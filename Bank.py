# importing modules
import mysql.connector

#creating database
mydb=mysql.connector.connect (host="localhost",user="root", passwd="Rohit@07", database ='rohitdb')
mycursor=mydb.cursor()

#creating required tables 
mycursor.execute("create table if not exists bank_master(acno char(4) primary key,name varchar(30),dob date,occu char(10),address varchar(200),mobileno char(10),adhar_no char(12),balance int(6))")
mycursor.execute("create table if not exists banktrans(acno char (4),amount int(6),dot date,ttype char(1),foreign key (acno) references bank_master(acno))")
mydb.commit()

while(True):    
    print('''\nMenu
1 --> Create account
2 --> Deposit money
3 --> Withdraw money
4 --> Display account
5 --> Close Account
6 --> Exit\n''')
    ch=int(input("Enter your choice:"))
    
#PROCEDURE FOR CREATING A NEW ACCOUNT OF THE APPLICANT
    if(ch==1):
        print("All information prompted are mandatory to be filled")
        acno=str(input("Enter account number:"))
        name=input("Enter name(limit 35 characters):")
        dob=str(input("Enter date of birth(YYYY-MM-DD): "))
        occu=input("Enter occupation:")
        address=str(input("Enter address:"))
        mobileno=str(input("Enter mobile no.:"))
        adhar_no=str(input('Enter the Aadhar number : '))
        balance=0
        mycursor.execute("insert into bank_master values('"+acno+"','"+name+"','"+dob+"','"+occu+"','"+address+"','"+mobileno+"','"+adhar_no+"','"+str(balance)+"')")
        mydb.commit()
        print("Account is successfully created!!!\n")
        
#PROCEDURE FOR UPDATIONG DETAILS AFTER THE DEPOSITION OF MONEY BY THE APPLICANT
    elif(ch==2):
        acno=str(input("Enter account number:"))
        dp=int(input("Enter amount to be deposited:"))
        dot=str(input("Enter date of Transaction(YYYY-MM-DD): "))
        ttype="d"
        mycursor.execute("insert into banktrans values('"+acno+"','"+str(dp)+"','"+dot+"','"+ttype+"')")
        mycursor.execute("update bank_master set balance=balance+'"+str(dp)+"' where acno='"+acno+"'")
        mydb.commit()
        print("money has been deposited successully!!!\n")
        
#PROCEDURE FOR UPDATING THE DETAILS OF ACCOUNT AFTER THE WITHDRAWL OF MONEY BY THE APPLICANT

    elif(ch==3):
        acno=str(input("Enter account number:"))
        wd=int(input("Enter amount to be withdrawn:"))
        dot=str(input("enter date of transaction(YYYY-MM-DD): "))
        ttype="w"
        mycursor.execute("insert into banktrans values('"+acno+"','"+str(wd)+"','"+dot+"','"+ttype+"')")
        mycursor.execute("update bank_master set balance=balance-'"+str(wd)+"' where acno='"+acno+"'")
        mydb.commit()

#PROCEDURE FOR DISPLAYING THE ACCOUNT OF THE ACCOUNT HOLDER AFTER HE/SHE ENTERS HIS/HER ACCOUNT NUMBER
    elif(ch==4):
        acno=str(input("Enter account number:"))
        mycursor.execute("select * from bank_master where acno='"+acno+"'")
        for i in mycursor:
            print(i)
#Closing Account            
    elif(ch==5):
        acno=str(input("Enter account number:"))
        mycursor.execute("Delete from banktrans where acno='"+acno+"'")
        mycursor.execute("Delete from bank_master where acno='"+acno+"'")
        print("Account has been closed\n")
        
    elif(ch==6):
        print("Thank You for using")
        break
    
    else:
        print("\nHy! That's Not A Number\n")
