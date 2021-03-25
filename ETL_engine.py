import xml.dom.minidom as dompar
import mysql.connector as mysql
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
        except Error as err:
            print(f"Error: '{err}'")
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
        q=[]
        for query in exe_seq:
            q.append(query.firstChild.data)
        return q

    def transform(self):
        Trans_det = self.doc.getElementsByTagName("TransformationDetails")[0].getElementsByTagName("TextTransformation")
        Arth_det = self.doc.getElementsByTagName("TransformationDetails")[0].getElementsByTagName("ArthimeticTransformation")
        tt=self.text_trans(Trans_det)
        at=self.arth_trans(Arth_det)
        return(tt,at)

    def text_trans(self,arr):
        tt_q=[]
        for tt in arr:
            attribute=tt.getElementsByTagName("attribute")[0].firstChild.data
            source = tt.getElementsByTagName("sourcePattern")[0].firstChild.data
            dest = tt.getElementsByTagName("destinationPattern")[0].firstChild.data
            table = "datawarehouse"
            tt_q.append("UPDATE {4} SET {0} = \"{1}\" where {2} = \"{3}\";".format(attribute,dest,attribute,source,table))
        return tt_q
                
    def arth_trans(self,arr):
        at_q=[]
        for at in arr:
            attribute=at.getElementsByTagName("attribute")[0].firstChild.data
            formula = at.getElementsByTagName("arthimeticFormulae")[0].firstChild.data
            table = "datawarehouse"
            at_q.append("UPDATE {2} SET {0} = {1};".format(attribute,formula,table))
        return at_q
        
    def load(self):
        exe_seq= self.doc.getElementsByTagName("DestinationDetails")[0]
        sql = self.doc.getElementsByTagName("DestinationInfo")[0]
        self.datawarehouse_db_name = sql.getElementsByTagName("name")[0].firstChild.data
        driver = sql.getElementsByTagName("driver")[0].firstChild.data
        protocol = sql.getElementsByTagName("protocol")[0].firstChild.data
        username= sql.getElementsByTagName("username")[0].firstChild.data
        password = sql.getElementsByTagName("password")[0].firstChild.data
        self.data_db = self.db_connection("localhost",username,password,self.datawarehouse_db_name)
 
        
    def run(self):
        self.select()
        q=self.extract()
        tt,at=self.transform()
        self.load()
        self.mycursor = self.my_db.cursor(buffered=True)
        self.datawarehouse_cursor = self.data_db.cursor(buffered=True)
        
        for qu in q:
            self.mycursor.execute(qu)
        for qu in tt:
            # print(qu)
            a = self.datawarehouse_cursor.execute(qu)
            self.data_db.commit()
        for qu in at:
            # print(qu)
            self.datawarehouse_cursor.execute(qu)
            self.data_db.commit()



if __name__ == "__main__" :
    e = ETLEngine("example.xml")
    e.run()
