import mysql.connector
class db:
    def initialize(self):
        # This method is to create the required  databases and tables
        con = mysql.connector.connect(host="localhost", user="root", passwd="root")
        cur=con.cursor()
        try:
            cur.execute("create database if not exists Hospital;")
            cur.execute("use Hospital;")
            cur.execute("create table if not exists doctor(id int,doc_name varchar(30),doc_specialization varchar(30),doc_phno bigint);")
            cur.execute("create table if not exists patient(id int,p_name varchar(30),p_address varchar(30),p_phno bigint,p_probdes varchar(50));")
            cur.execute("create table if not exists medicine(id int,m_name varchar(20),m_drugs_involved varchar(50),diseases_can_be_cured varchar(30));")
            print("initialization is done")
            cur.execute("select * from doctor")
            res=cur.fetchall()
        except:
            con.rollback()
        cur.close()
        con.close()
        return res
    def insert(self,table,tpl):
        con=mysql.connector.connect(host="localhost",user="root",passwd="root",database="Hospital")
        cur=con.cursor()
        if(table=="doctor" or table=="medicine"):
            try:
                st="insert into "+table+" values(%s,%s,%s,%s)"
                cur.execute(st,tpl)
                con.commit()
                print("insertion into table "+table+" is successful")
                cur.execute("select * from " + table)
                res = cur.fetchall()
            except:
                con.rollback()

        else:
            try:
                st="insert into "+table+" values(%s,%s,%s,%s,%s)"
                cur.execute(st,tpl)
                con.commit()
                print("insertion into table " + table + " is successful")
                cur.execute("select * from "+table)
                res=cur.fetchall()
            except:
                con.rollback()
        cur.close()
        con.close()
        return res
    def read(self,table):
        con=mysql.connector.connect(host="localhost",user="root",passwd="root",database="Hospital")
        cur=con.cursor()
        try:
            cur.execute("select * from "+table)
            res=cur.fetchall()
            if(len(res)==0):
                print("No data Found")
            else:
                for i in res:
                    print(i)
        except:
            con.rollback()
        cur.close()
        con.close()
        return res
    def update(self,table,id,col,new):
        con=mysql.connector.connect(host="localhost",user="root",passwd="root",database="Hospital")
        cur=con.cursor()
        try:
            st="update "+table+" set "+col+" ='"+str(new)+"' where  id="+str(id)
            cur.execute(st)
            con.commit()
            print("updation successful")
            cur.execute("select * from "+table)
            res=cur.fetchall()
        except:
            con.rollback()
        cur.close()
        con.close()
        return res
    def delete(self,table,id):
        con = mysql.connector.connect(host="localhost", user="root", passwd="root", database="Hospital")
        cur=con.cursor()
        try:
            st="delete from "+table+" where id="+str(id)
            cur.execute(st)
            con.commit()
            print("deletion successful")
            cur.execute("select * from "+table)
            res=cur.fetchall()
        except:
            con.rollback()
        cur.close()
        con.close()
        return res