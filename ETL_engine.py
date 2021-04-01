import xml.dom.minidom as dompar
import mysql.connector as mysql
import sql_metadata, re
import pandas as pd
class ETLEngine:
    def __init__(self,xmlFile):
        self.doc = dompar.parse(xmlFile)
        sql = self.doc.getElementsByTagName("SQL")
        ftp = self.doc.getElementsByTagName("FTP")
        self.isSQL=(ftp==[]) and (sql != [])
        self.isFTP=(ftp!=[]) and (sql == [])

    def db_connection(self,hostname,username,password,db):
        connection = None
        try:
            connection = mysql.connect(
                host = hostname,
                username = username,
                password = password,
                database = db
            )
            print("Connected to database "+ db)
        except Exception as e:
            print(e)
        return connection
        
    def select(self):
        if(self.isSQL):
            sql = self.doc.getElementsByTagName("SQL")[0]
            self.usr_db_name = sql.getElementsByTagName("name")[0].firstChild.data
            driver = sql.getElementsByTagName("driver")[0].firstChild.data
            username= sql.getElementsByTagName("username")[0].firstChild.data
            password = sql.getElementsByTagName("password")[0].firstChild.data
            self.my_db = self.db_connection("localhost",username,password,self.usr_db_name)
        elif(isFTP):
            print("Coming Soon")

    def extract(self):
        exe_seq= self.doc.getElementsByTagName("ExecutionSequence")[0].getElementsByTagName("Query")
        q = []
        self.srcColumns = []
        df = pd.DataFrame()
        self.srcData = []
        self.table = ""
        for query in exe_seq:
            q.append(query.firstChild.data)
        for qu in q:
            self.table = re.search('(?<=from )(\w+)', qu).group(1)
            # from_str = re.search('(?<=select )(.*)(?=from)', qu).group(1)
            # self.srcColumns = [x.strip() for x in from_str.split(',')]
            self.mycursor.execute(qu)
            myresult = self.mycursor.fetchall()
            for x in myresult:
                self.srcData.append(x)
        # print(type(columns))
        # self.mycursor.execute()
        return q

    def transform(self):
        Trans_det = self.doc.getElementsByTagName("TransformationDetails")[0].getElementsByTagName("TextTransformation")
        Arth_det = self.doc.getElementsByTagName("TransformationDetails")[0].getElementsByTagName("ArthimeticTransformation")
        Null_det = self.doc.getElementsByTagName("TransformationDetails")[0].getElementsByTagName("NullTransformation")
        tt=self.text_trans(Trans_det)
        at=self.arth_trans(Arth_det)
        return(tt,at)

    def text_trans(self,arr):
        tt_q=[]
        # table = "employee"
        for tt in arr:
            sourceAttribute=tt.getElementsByTagName("sourceAttribute")[0].firstChild.data
            destinationAttribute=tt.getElementsByTagName("destinationAttribute")[0].firstChild.data
            source = tt.getElementsByTagName("sourcePattern")[0].firstChild.data
            dest = tt.getElementsByTagName("destinationPattern")[0].firstChild.data
            tt_q.append("UPDATE {3} SET {0} = \"{1}\" where {0} = \"{2}\";".format(sourceAttribute,dest,source,self.table))
            tt_q.append("ALTER TABLE {2} RENAME COLUMN {0} TO {1};".format(sourceAttribute,destinationAttribute,self.table))
        return tt_q
                
    def arth_trans(self,arr):
        at_q=[]
        # table = "employee"
        for at in arr:
            sourceAttribute=at.getElementsByTagName("sourceAttribute")[0].firstChild.data
            destinationAttribute=at.getElementsByTagName("destinationAttribute")[0].firstChild.data
            attribute=at.getElementsByTagName("attribute")[0].firstChild.data
            formula = at.getElementsByTagName("arthimeticFormulae")[0].firstChild.data
            at_q.append("UPDATE {2} SET {0} = {1};".format(sourceAttribute,formula,self.table))
            at_q.append("ALTER TABLE {2} RENAME COLUMN {0} TO {1};".format(sourceAttribute,destinationAttribute,self.table))
        return at_q
        
    def null_trans(self,arr):
        nt_q = []
        for nt in arr:
            sourceAttribute=nt.getElementsByTagName("sourceAttribute")[0].firstChild.data
            destinationAttribute=nt.getElementsByTagName("destinationAttribute")[0].firstChild.data
            nt_q.append("ALTER TABLE {2} RENAME COLUMN {0} TO {1};".format(sourceAttribute,destinationAttribute,self.table))
        return nt_q
        

    def mapping(self):
        maps_arr = []
        table =self.datawarehouse_db_name
        all_maps = self.doc.getElementsByTagName("Mapping")[0].getElementsByTagName("Map")
        sourceAttributes=[]
        destinationAttributes=[]
        for m in all_maps:
            old_name = m.getElementsByTagName("source")[0].firstChild.data
            new_name = m.getElementsByTagName("Destination")[0].firstChild.data
            type_query = "SELECT DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{0}' AND COLUMN_NAME = '{1}' ".format(self.usr_db_name,old_name)
            self.mycursor.execute(type_query)
            myresult = self.mycursor.fetchall()
            if(myresult[0][0]=="varchar"):
                maps_arr.append("ALTER TABLE {1} ADD {0} varchar(255);".format(new_name,table))
            else:
                maps_arr.append("ALTER TABLE {1} ADD {0} {2};".format(new_name,table,myresult[0][0]))
            sourceAttributes.append(old_name)
            destinationAttributes.append(new_name)
        return maps_arr,sourceAttributes,destinationAttributes

    def load(self):
        sql= self.doc.getElementsByTagName("DestinationDetails")[0].getElementsByTagName("DestinationInfo")[0]
        self.datawarehouse_db_name = sql.getElementsByTagName("name")[0].firstChild.data
        driver = sql.getElementsByTagName("driver")[0].firstChild.data
        protocol = sql.getElementsByTagName("protocol")[0].firstChild.data
        username= sql.getElementsByTagName("username")[0].firstChild.data
        password = sql.getElementsByTagName("password")[0].firstChild.data
        # database connection
        self.data_db = self.db_connection("localhost",username,password,self.datawarehouse_db_name)
        self.datawarehouse_cursor = self.data_db.cursor(buffered=True)
        maps_arr,sourceAttributes,destinationAttributes = self.mapping()
        for m in maps_arr:
            print(m)
            self.datawarehouse_cursor.execute(m)
        # loadQuery="INSERT into {0} (".format(self.datawarehouse_db_name)
        # for i in self.srcColumns:
        #     loadQuery+=i
        # loadQuery+=") values ("
        # for i in range(len(self.srcData)):

        return maps_arr
 
        
    def run(self):
        self.select()
        self.mycursor = self.my_db.cursor(buffered=True)
        q = self.extract()
        maps_arr = self.load()
        text_transform,arith_transform = self.transform()
        # for qu in q:
        #     self.mycursor.execute(qu)
        #     # print(sql_metadata.get_query_columns(qu))
        #     myresult = self.mycursor.fetchall()
        #     for x in myresult:
        #         print(x)

        for qu in text_transform:
            self.mycursor.execute(qu)
            myresult = self.mycursor.fetchall()
            print(myresult)
            for x in myresult:
                print(x)
            # self.data_db.commit()

        for qu in arith_transform:
            self.mycursor.execute(qu)
            self.data_db.commit()
        
        
            # self.data_db.commit()


if __name__ == "__main__" :
    e = ETLEngine("example.xml")
    e.run()
