import xml.dom.minidom as dompar
import mysql.connector as mysql
class ETLEngine:
    def __init__(self,xmlFile):
        self.doc = dompar.parse(xmlFile)
        sql = self.doc.getElementsByTagName("SQL")
        ftp = self.doc.getElementsByTagName("FTP")
        self.isSQL=(ftp==[]) and (sql != [])
        self.isFTP=(ftp!=[]) and (sql == [])
        
    def select(self):
        if(self.isSQL):
            sql = self.doc.getElementsByTagName("SQL")[0]
            self.s_name = sql.getElementsByTagName("name")[0].firstChild.data
            s_driver = sql.getElementsByTagName("driver")[0].firstChild.data
            self.s_username= sql.getElementsByTagName("username")[0].firstChild.data
            self.s_password = sql.getElementsByTagName("password")[0].firstChild.data
            
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
            tt_q.append("UPDATE {4} SET {0} = \"{1}\" where {2} = \"{3}\";".format(attribute,dest,attribute,source,self.s_name))
        return tt_q
                
    def arth_trans(self,arr):
        at_q=[]
        for at in arr:
            attribute=at.getElementsByTagName("attribute")[0].firstChild.data
            formula = at.getElementsByTagName("arthimeticFormulae")[0].firstChild.data
            at_q.append("UPDATE {2} SET {0} = {1};".format(attribute,formula,self.s_name))
        return at_q
        
    def load():
        pass
        
    def run(self):
        self.select()
        q=self.extract()
        tt,at=self.transform()
        my_db = mysql.connect(
                host="localhost",
                username=self.s_username,
                password=self.s_password,
                database= self.s_name
            )
        self.mycursor = my_db.cursor(buffered=True)
        
        for qu in tt:
            # print(qu)
            self.mycursor.execute(qu)
            # my_db.commit()
        for qu in at:
            # print(qu)
            self.mycursor.execute(qu)
            # my_db.commit()
        for qu in q:
            self.mycursor.execute(qu)
            
        for x in self.mycursor:
            print(x)



if __name__ == "__main__" :
    e = ETLEngine("template.xml")
    e.run()
