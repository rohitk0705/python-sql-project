import os
import platform
import mysql.connector as mysql

mydb=mysql.connect(host='localhost',user='root',password='Rohit@07',database='rohitdb')
mycursor=mydb.cursor()
mycursor.execute('''create table if not exists ACCOUNT(Accno numeric(14) PRIMARY KEY,Name varchar(24),Age int(2),Occu varchar(24),Address varchar(50),Mob numeric(10),Aadhar_no numeric(12),Amt int(7),AccType char(10))''')
mycursor.execute('create table if not exists Amount(Accno numeric(14),Amtdeposit numeric(7),Month char(10),FOREIGN KEY (Accno) REFERENCES ACCOUNT(Accno))')

def AccInsert():
    try:
        L=[]
        Accno=int(input('Enter the Account number : '))
        L.append(Accno)
        name=input('Enter the Customer Name: ')
        L.append(name)
        age=int(input('Enter Age of Customer : '))
        L.append(age)
        occup=input('Enter the Customer Occupation :')
        L.append(occup)
        Address=input('Enter the Address of the Customer : ')
        L.append(Address)
        Mob=int(input('Enter the Mobile number : '))
        L.append(Mob)
        Aadhar_no=int(input('Enter the Aadhar number : '))
        L.append(Aadhar_no)
        Amt=float(input('Enter the Money Deposited :'))
        L.append(Amt)
        AccType=input('Enter the Account Type (Saving/RD/PPF/Current) :')
        L.append(AccType)
        cust=(L)
        sql='''insert into ACCOUNT(Accno,Name,Age,Occu,Address,Mob,Aadhar_no,Amt,AccType)values(%s,%s,%s, %s,%s,%s, %s,%s,%s)'''
        mycursor.execute(sql,cust)
    except:
        print("error")
        mydb.rollback()
        return
    mydb.commit()
    

def AccView():
    print('''Select the search criteria : 
    1. Acc no
    2. Name
    3. Mobile
    4. Aadhar
    5. View All''')
    ch=int(input('Enter the choice : '))
    if ch==1:
        s=int(input('Enter ACC no : '))
        rl=(s,)
        sql='select * from account where Accno=%s'
        mycursor.execute(sql,rl)
    elif ch==2:
        s=input('Enter Name : ')
        rl=(s,)
        sql='select * from account where Name=%s'
        mycursor.execute(sql,rl)
    elif ch==3:
        s=int(input('Enter Mobile No : '))
        rl=(s,)
        sql='select * from account where Mob=%s'
        mycursor.execute(sql,rl)
    elif ch==4:
        s=input('Enter Adhar : ')
        rl=(s,)
        sql='select * from account where Aadhar_no=%s'
        mycursor.execute(sql,rl)
    elif ch==5:
        sql='select * from account'
        mycursor.execute(sql)
    res=mycursor.fetchall()
    print('The Customer details are as follows : ')

def AccDeposit():
    L=[]
    Accno=int(input('Enter the Account number : '))
    L.append(Accno)
    Amtdeposit=eval(input('Enter the Amount to be deposited : '))
    L.append(Amtdeposit)
    month=input('Enter month of Salary : ')
    L.append(month)
    cust=(L)
    sql='Insert into Amount(Accno,Amtdeposit,Month) values(%s,%s,%s)'
    mycursor.execute(sql,cust)
    mydb.commit()

def AccView():
    print('Please enter the details to view the Money details :')
    Accno=int(input('Enter the Account number of the Customer whose amount is to be viewed : '))
    sql='''Select Account.Accno, Account.Name,Account.Age,Account.Occu,Account.Address,Account.Mob,Account.Aadhar_no,Account.Amt,Account.AccType,sum(Amount.Amtdeposit)
 from Account INNER JOIN Amount ON Account.Accno=Amount.Accno and Amount.Accno = %s'''
    rl=(Accno,)
    mycursor.execute(sql,rl)
    res=mycursor.fetchall()
    for x in res:
        print(x)

def AllAcc():
    sql='''Select * from Account natural join Amount '''
    mycursor.execute(sql)
    res=mycursor.fetchall()
    for x in res:
        print(x)

def closeAcc():
    Accno=int(input('Enter the Account number of the Customer to be closed : '))
    rl=(Accno,)
    sql='Delete from Amount where Accno=%s'
    mycursor.execute(sql,rl)
    sql='Delete from Account where Accno=%s'
    mydb.commit()

def MenuSet():
    print('Enter 1 : To Add Customer')
    print('Enter 2 : To View Customer ')
    print('Enter 3 : To Deposit Money ')
    print('Enter 4 : To Close Account')
    print('Enter 5 : To View All Customer Details')
    try:
        userInput = int(input("Please Select An Above Option: "))
    except ValueError:
        print("\nHy! That's Not A Number")
    else:
        print("\n")
        if(userInput == 1):
            AccInsert()
        elif (userInput==2):
            AccView()
        elif (userInput==3):
            AccDeposit()
        elif (userInput==4):
            closeAcc()
        elif (userInput==5):
            AllAcc()
        else:
            print('Enter correct choice. . .')

MenuSet()

def runAgain():
    runAgn = input('\nwant To Run Again Y/N: ')
    while(runAgn.lower() == 'Y','y'):
        if(platform.system() == 'Windows'):
            print(os.system('cls'))
        else:
            print(os.system('clear'))

        MenuSet()

runAgain()
