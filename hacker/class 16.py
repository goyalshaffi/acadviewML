import sqlite3
conn = sqlite3.connect('test.db')
print("opened database successfully")

#conn.execute('''CREATE TABLE COMPANY
           # (ID INT PRIMARY KEY  NOT NULL,
            #NAME     TEXT  NOT NULL,
            #AGE      INT    NOT NULL,
            #ADDRESS  CHAR(50)   NOT NULL,
            #SALARY   REAL)''')
#print("table created")
#conn.close()
#conn.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY)\
 #           VALUES(1,'KAV',20,'ZIRAKPUR',0)")
#conn.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY)\
 #          VALUES(1,'KAV1',20,'ZIRAKPUR',2000)")
conn.commit()
#print("recorded")
#conn.close()
#conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
#conn.commit()
#print("changes",conn.total_changes)
conn.execute("DELETE FROM COMPANY where ID=1")
conn.commit()
print("changes",conn.total_changes)

cursor=conn.execute("SELECT ID,NAME,AGE,SALARY,ADDRESS from COMPANY")
for row in cursor:
    print("ID=",row[0])
    print("NAME =",row[1])
    print("AGE=", row[2])
    print("SALARY =", row[3])
    print("ADDRESS=", row[4],"\n")
print("successful")
print(cursor)

#conn.close()

