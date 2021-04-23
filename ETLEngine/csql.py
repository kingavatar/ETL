import csv
import mysql.connector as mysql
import pandas as pd

my_db=mysql.connect(host="localhost",
username="osurihimeshkrishna",
password="password",
database="airbase")



with open ('employee.csv', 'r') as f:
    data=pd.read_csv(f)
    # print(data)
    df=pd.DataFrame(data)
    # print(df.dtypes)
    # print(df.columns)
    create_query="create table temp ("
    k=0
    for i in df.columns:
        create_query = create_query + str(i).replace('"',"")+" "
        if(df.dtypes[k]=="int64"):
            create_query = create_query + "int ,"
        elif(df.dtypes[k] == "object"):
            create_query = create_query + "varchar(255),"
        k=k+1
    create_query=create_query[:-1]+")"
    # print(create_query)
    cursor = my_db.cursor()
    cursor.execute("drop table temp;")
    cursor.execute(create_query)
    myresult=[]
    for i in range(len(df)):
        temp_result=[]
        for j in range(len(df.columns)):
            if(type(df.iloc[i][j])=="int64"):
                temp_result.append(int(df.iloc[i][j]))
            else:
                temp_result.append(str(df.iloc[i][j]))
        temp_result=tuple(temp_result)
        myresult.append(temp_result)
    
    attr=""
    values=""
    # columns=[]
    for i in df.columns:
        attr=attr+i+","
        values=values+"%s,"
    attr=attr[:-1]
    values=values[:-1]
    str_query="INSERT INTO temp ({0}) VALUES ({1}) ".format(attr,values)
    mySql_insert_query = """{0}""".format(str_query)
    print(mySql_insert_query)
    cursor.executemany(mySql_insert_query, myresult)
    my_db.commit()
    # for i in df:
    #     print(i)
    # reader = csv.reader(f)
    # data = next(reader)
    # query = 'insert into temp {0} values ({1})'
    # # query = query.format(','.join("%s" * len(data)))
    
    # # print(data)
    
    # query1=query1.format(attr)
    # coursor
    # # for data in reader:
    # cursor.execute(query1)
    # cursor.commit()