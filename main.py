import dbCRUD
mydb=dbCRUD.db()
mydb.initialize()
while(True):
    print("Please select the operation You want to do on the database:")
    print("1.Insert into table\n2.Read from the table\n3.Update the table\n4.Delete from the table\n5.exit")
    ch=int(input())
    if(ch==1):
        print("Select the table to insert:\n1.doctor\n2.medicine\n3.patient")
        ch2=int(input())
        if(ch2==1):
            lst=[]
            lst.append(int(input("Enter Doctor ID:\n")))
            lst.append(input("Enter Doctor Name:\n"))
            lst.append(input("Enter Doctor Specialization:\n"))
            lst.append(input("Enter Doctor Phone Number:\n"))
            mydb.insert("doctor",tuple(lst))
        elif(ch2==2):
            lst=[]
            lst.append(int(input("Enter medicine ID:\n")))
            lst.append(input("Enter medicine Name:\n"))
            lst.append(input("Enter medicine Drug Involved:\n"))
            lst.append(input("Enter the Diseases can be cured by this medicine:\n"))
            mydb.insert("medicine", tuple(lst))
        else:
            lst = []
            lst.append(int(input("Enter patient ID:\n")))
            lst.append(input("Enter patient Name:\n"))
            lst.append(input("Enter patient Address:\n"))
            lst.append(input("Enter patient Phone Number:\n"))
            lst.append(input("Enter the Patient Problem Description:\n"))
            mydb.insert("patient", tuple(lst))
    elif(ch==2):
        print("Enter the table number you want to view the data:\n1.doctor\n2.patient\n3.medicine")
        ch2=int(input())
        if(ch2==1):
            mydb.read("doctor")
        elif(ch==2):
            mydb.read("patient")
        else:
            mydb.read("medicine")
    elif(ch==3):
        print("Enter the table number you want to Update the data:\n1.doctor\n2.patient\n3.medicine")
        ch2 = int(input())
        if (ch2 == 1):
            mydb.update("doctor",int(input("Enter the id of the doctor:")),input("Enter the Column you want to Update:"),input("Enter the new value in the Column:"))
        elif (ch == 2):
            mydb.update("patient",int(input("Enter the id of the patient:")),input("Enter the Column you want to Update:"),input("Enter the new value in the Column:"))
        else:
            mydb.update("medicine",int(input("Enter the id of the medicine:")),input("Enter the Column you want to Update:"),input("Enter the new value in the Column:"))
    elif(ch==4):
        print("Enter the table number you want to delete the data:\n1.doctor\n2.patient\n3.medicine")
        ch2 = int(input())
        if (ch2 == 1):
            mydb.delete("doctor",int(input("Enter the ID of the Doctor to delete from the database:")))
        elif (ch == 2):
            mydb.delete("patient",int(input("Enter the ID of the patient to delete from the database:")))
        else:
            mydb.delete("medicine",int(input("Enter the ID of the medicine to delete from the database:")))
    else:
        break
