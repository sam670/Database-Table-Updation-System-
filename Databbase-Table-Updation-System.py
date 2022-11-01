############## This is a user input base system you can update your mysql databse table
## data without using any query of sql

#### STEPS TO USE THIS TOOL

#1-you have to select the given column name which you wnat to update
## Like - rno ,name and marks

##2- give the current input by watching the table.

##3 - after one updation this will ask you to do the updation again or not

##4 - write yes to countinue otherwise write no

'''
this is the table type and table name is 'student1':
+------+------+-------+
| rno  | name | marks |
+------+------+-------+
|    1 | sam  |    96 |
|    2 | ravi |    89 |
|    3 | bahu |    99 |
+------+------+-------

'''

import colorama
import mysql.connector as s
import colorama
from colorama import Fore

con = s.connect(host="localhost", user="USER-NAME", password="MYSQL-PASSWORD", database="DATABASE-NAME")

cur = con.cursor()

#showing table data before updation
print("This is the table , which data you want to update")
cur.execute("select * from student1")
for i in cur:
    print(i)

print("\n")
#updateing the tbale data
while True:
    data = input(Fore.RED + "what you want to update(rno/name/marks) : ")
    if data=='rno':
        name = input("student1 name , whome roll number do you want to update : ")
        rno = int(input("Enter new Roll number : "))
        qu = "update student set rno={0} where name='{1}'".format(rno,name)
        cur.execute(qu)
        con.commit()

        try:
            if cur.rowcount > 0:
                print(name, ",Roll number updated and now the roll number is", rno)
                cur.execute("select * from student1")
                for i in cur:
                    print(i)
        except:
            test = input(Fore.RED + "Do you want to countinue(yes/no): ")
            if test == 'yes':
                continue
            else:
                break


    elif data=='name':
        rno = input("Enter student roll number whose name you want to update : ")
        name = input("Enter new name : ")
        qu = "update student1 set name='{0}' where rno={1}".format(name,rno)
        cur.execute(qu)
        con.commit()

        if cur.rowcount>0:
            print(rno,",name updated and now the name is",name)
            print(Fore.GREEN + "The updated table \n")
            cur.execute("select * from student1")
            for i in cur:
                print(i)
        else:
            print(Fore.RED + "\nSorry, This \'"+rno+"\' roll number is not in the table that you want to update......\n")
            #continue
            test = input(Fore.RED + "Do you want to countinue(yes/no): ")
            if test=='yes':
                continue
            else:
                break


    elif data=='marks':
        name = input("student name , whose marks you want to update : ")
        marks = int(input("Enter new marks : "))
        qu = "update student1 set marks={0} where name='{1}'".format(marks,name)
        cur.execute(qu)
        con.commit()
        if cur.rowcount>0:
            print(Fore.GREEN + name, ",marks updated and now the marks is", marks)
            print(Fore.GREEN + "The updated table \n")
            cur.execute("select * from student1")
            for i in cur:
                print(i)
        else:
            print(Fore.RED + "\nSorry, This \'"+name+"\' name is not in the table that you want to update......\n")
            
            #continue
            test = input(Fore.RED + "Do you want to countinue(yes/no): ")
            if test=='yes':
                continue
            else:
                break

    else:
        print(Fore.RED + "Sorry , We don't have any data like ")
    num = input(Fore.RED + "Do you want to updated any other data(yes/no) : ")
    if num=="yes":
        continue
    else:
        break

print("\n")
print(Fore.GREEN + "data updated successfully.....")
