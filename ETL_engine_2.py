import xml.dom.minidom as dompar
import mysql.connector as mysql
import sql_metadata, re
import pandas as pd
class ETLEngine:
    def __init__(self,xmlFile):
        self.dict={}
        self.srcColumns=[]
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
        
    def select(self,i):
        if(self.isSQL):
            sql = i.getElementsByTagName("SQL")[0]
            self.usr_db_name = sql.getElementsByTagName("name")[0].firstChild.data
            driver = sql.getElementsByTagName("driver")[0].firstChild.data
            username= sql.getElementsByTagName("username")[0].firstChild.data
            password = sql.getElementsByTagName("password")[0].firstChild.data
            self.my_db = self.db_connection("localhost",username,password,self.usr_db_name)
        elif(isFTP):
            print("Coming Soon")


    def extract(self,i):
        exe_seq= i.getElementsByTagName("ExtractSequence")[0].getElementsByTagName("Query")
        q = []
        for query in exe_seq:
            q.append(query.firstChild.data)
        #extracting table,columns from query
        # self.mycursor.execute("CREATE table query(val int);")
        self.mycursor.execute("DROP table query;")
        upd_query="CREATE table query as "+q[0]+";"
        self.mycursor.execute(upd_query)
        self.mycursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = \"query\"")
        col=self.mycursor.fetchall()
        self.srcColumns=[]
        for i1 in col:
            for j in i1:
                self.srcColumns.append(j)
        # print(self.srcColumns)
        self.table= "query";
        # for qu in q:
        #     self.table = re.search('(?<=from )(\w+)', qu).group(1)
        #     from_str = re.search('(?<=select )(.*)(?=from)', qu).group(1)
        #     self.srcColumns = [x.strip() for x in from_str.split(',')]
        
        
        #extracting destination details    
        sql= self.doc.getElementsByTagName("DestinationDetails")[0].getElementsByTagName("DestinationInfo")[0]
        self.datawarehouse_db_name = sql.getElementsByTagName("name")[0].firstChild.data
        driver = sql.getElementsByTagName("driver")[0].firstChild.data
        protocol = sql.getElementsByTagName("protocol")[0].firstChild.data
        username= sql.getElementsByTagName("username")[0].firstChild.data
        password = sql.getElementsByTagName("password")[0].firstChild.data
        self.dsttable= i.getElementsByTagName("ExtractSequence")[0].getElementsByTagName("DstTable")[0].firstChild.data
        # datawarehouse connection
        self.data_db = self.db_connection("localhost",username,password,self.datawarehouse_db_name)
        self.datawarehouse_cursor = self.data_db.cursor(buffered=True)
        return q[0]
            

    
    def transform(self,i):
        Trans_det = i.getElementsByTagName("TransformationDetails")[0].getElementsByTagName("TextTransformation")
        Arth_det = i.getElementsByTagName("TransformationDetails")[0].getElementsByTagName("ArthimeticTransformation")
        Null_det = i.getElementsByTagName("TransformationDetails")[0].getElementsByTagName("NullTransformation")
        tt=self.text_trans(Trans_det)
        at=self.arth_trans(Arth_det)
        nt=self.null_trans(Null_det)
        return(tt,at)

    def text_trans(self,arr):
        tt_q=[]
        table = self.table
        for tt in arr:
            sourceattribute=tt.getElementsByTagName("sourceAttribute")[0].firstChild.data
            destattribute=tt.getElementsByTagName("destinationAttribute")[0].firstChild.data
            self.dict.update({sourceattribute:destattribute})
            source = tt.getElementsByTagName("sourcePattern")[0].firstChild.data
            dest = tt.getElementsByTagName("destinationPattern")[0].firstChild.data
            tt_q.append("UPDATE {4} SET {0} = \"{1}\" where {2} = \"{3}\";".format(sourceattribute,dest,sourceattribute,source,table))
        return tt_q
                
    def arth_trans(self,arr):
        at_q=[]
        table = self.table
        for at in arr:
            sourceattribute=at.getElementsByTagName("sourceAttribute")[0].firstChild.data
            destattribute=at.getElementsByTagName("destinationAttribute")[0].firstChild.data
            self.dict.update({sourceattribute:destattribute})
            formula = at.getElementsByTagName("arthimeticFormulae")[0].firstChild.data
            at_q.append("UPDATE {2} SET {0} = {1};".format(sourceattribute,formula,table))
        return at_q
        
    def null_trans(self,arr):
        nt_q=[]
        table=self.table
        for nt in arr:
            sourceattribute=nt.getElementsByTagName("sourceAttribute")[0].firstChild.data
            destattribute=nt.getElementsByTagName("destinationAttribute")[0].firstChild.data
            self.dict.update({sourceattribute:destattribute})
        return 0
 
        
    def run(self):
        try :
            et=self.doc.getElementsByTagName("ET")
        except:
            return "problem with ET","ERROR"
        for i in et:
            try:
                self.select(i)
            except:
                return "problem with select","ERROR"
            try:
                self.mycursor = self.my_db.cursor(buffered=True)
            except:
                return "problem with mycursor","ERROR"
            try:
                q = self.extract(i)
            except:
                return "problem with extraction","ERROR"
        
            try:
                tt,at=self.transform(i)
            except:
                return "problem with transform","ERROR"
                # print("problem with transform")
                # return "problem with transform","ERROR"
        
            for qu in tt:
                # print(qu)
                try:
                    self.mycursor.execute(qu)
                except:
                    return "problem with text tranform execute","ERROR"
                    # print("Problem with transform execute")
                    #if a new mapping is given which is not present in the select statement this will show an error
                    # return "problem with text tranform execute","ERROR"
            for qu in at:
                try:
                    self.mycursor.execute(qu)
                except:
                    return "problem with arthimetic transform execute","ERROR"
            # print(self.dict)
            try:
                self.mycursor.execute("select * from query")
            except:
                return "Last execute query","ERROR"
            
            try:
                self.my_db.commit()
                myresult = self.mycursor.fetchall()
            except:
                return "db commit error","ERROR"
            
            # i=input()
        # self.datawarehouse_cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = \"datawarehouse\"")
        # col=self.datawarehouse_cursor.fetchall()
        # dw_columns=[]
        # for i in col:
        #     for j in i:
        #         dw_columns.append(j)
        # print(dw_columns)
            insert_1=""
            values=""
        # for i in dw_columns:
        #     insert_1=insert_1+ i +","
        #     values=values+"%s,"
        # insert_1=insert_1[:-1]
        # values=values[:-1]
            try:
                for i in self.srcColumns:
                    if(i in self.dict):
                        insert_1=insert_1+ self.dict[i] +","
                        values=values+"%s,"
                insert_1=insert_1[:-1]
                values=values[:-1]
            except:
                return "problem with srcColumns","ERROR"
                # print("ERROR with srcColumns")
                
            # print(insert_1)
            # print(values)
            try:
                str_query="INSERT INTO {2} ({0}) VALUES ({1}) ".format(insert_1,values,self.dsttable)
            except:
                return "problem with str_query","ERROR"
                # print("There maybe some parameter with no transformation")
                
            mySql_insert_query = """{0}""".format(str_query)
            # print(myresult)
            try:
                self.datawarehouse_cursor.executemany(mySql_insert_query, myresult)
                self.data_db.commit()
            except:
                return "datawarehouse execute error","ERROR"
                # print("There maybe some parameter with no transformation")
                
            # print("Success")
        return "","SUCCESS"
                   

if __name__ == "__main__" :
    e = ETLEngine("example_2.xml")
    e.run()
