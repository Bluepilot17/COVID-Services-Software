from prettytable import PrettyTable
import pickle
import random
import sys
def addhos():
 fp1 = open("addhos.dat", "ab+")
 global hcode,hname,htype,hhrs,hrate,hphone,hadd
 hcode = int(input("Enter Hospital Code : "))
 hname = input("Enter Hospital Name : ")
 htype=input("Enter Hospital type (pvt/govt) : ")
 hhrs=input("Enter no. of hours : ")
 hrate=input("Enter rating of hospital : ")
 hphone=int(input("Enter phone no. : "))
 hadd=input("Enter Hospital address : ")
 y=PrettyTable()
 y.field_names=["Hospital Code","Hospital Name","Type","Hours","Rating","Phone
Number","Address"]
 y.add_row([hcode,hname,htype,hhrs,hrate,hphone,hadd])
 print(y)
 l=y.get_string()
 pickle.dump(l, fp1)
 try:
 reader1 = pickle.load(fp1)
 except:
 fp1.close()
def hoslist():
 fp2=open("hoslist.dat","ab+")
 y=PrettyTable(["Hospital Code","Hospital Name","Type","Hours","Rating","Phone
Number","GT Road,Jabalpur,MP"])
 y.add_row(["9876546","Civil Hospital","Private","24
Hrs","4.8","9111093232","Gandhi Road,Khandwa,MP"])
 y.add_row(["1107654","Military Hospital","Government","24
Hrs","4.7","9001825643","Mandla Highway,Indore,MP"])
 y.add_row(["9077343","H R Hospital","Government","24
Hrs","4.6","8944235661","MT Chowk,Bhopal,MP"])
 y.add_row(["8766541","Marble City Hospital","Private"," 24
Hrs","4.3","9018277654","Vinod Gate,Gwalior,MP"])
 y.add_row(["9098116","Dayanand Hospital","Government"," 24
Hrs","4.1","9190876811","Bose Nagar,Indore,MP"])
 y.add_row(["7445332","Aayushman Hospital","Government"," 24
Hrs","4.0","8978812442","Ad Road,Jabalpur,MP"])
 y.add_row(["8908965","Victoria Hospital","Private"," 24
Hrs","4.0","9871290181","Modi Bara,Betul,MP"])
 # y.add_row([hcode,hname,htype,hhrs,hrate,hphone,hadd])
 print(y)
 l=y.get_string()
 pickle.dump(l,fp2)
 try:
 reader1 = pickle.load(fp2)
 except:
 fp2.close()
def pay():
 print("How would you like to pay?")
 print()
 print()
 print("Please refer to following codes : ")
 print()
 print("{:<10} {:<10}".format('Code', 'Payment Option'))
 print("-------------------------------------------")
 print("{:<10} {:<10}".format('1', 'Net Banking'))
 print("{:<10} {:<10}".format('2', 'Credit/Debit Card'))
 print("___________________________________________")
 print()
 payment=int(input("Enter suitable code : "))
 print()
 if payment==1:
 print()
 print("Please select a bank")
 print()
 print()
 print("{:<10} {:<10}".format('Code', 'Bank Name'))
 print("-------------------------------------------")
 print("{:<10} {:<10}".format('1', 'HDFC Bank'))
 print("{:<10} {:<10}".format('2', 'State Bank of India'))
 print("{:<10} {:<10}".format('3', 'ICICI Bank'))
 print("{:<10} {:<10}".format('4', 'Syndicate Bank'))
 print()
 z=input("Enter name of your prefered bank : ")
 print()
 act=int(input("Enter account no. : "))
 print()
 pin=int(input("Enter your pin : "))
 print()
 print("Payment Sucessfull!")
 else:
 nu=int(input("Enter card number : "))
 print()
 cvv=int(input("Enter cvv : "))
 print()
 pin=int(input("Enter your pin :"))
 print()
 print("Payment Sucessfull!")
def dose():
 global fp,state,dist,pin,age
 fp=open("vacdose.dat","ab+")
 state=input("Enter State :")
 dist=input("Enter District :")
 pin=int(input("Enter PIN Code :"))
 age=int(input("Enter Age :"))
 if age>=18:
 l=[state,dist,pin,age]
 pickle.dump(l,fp)
 try:
 reader=pickle.load(fp)
 except:
 fp.close()
 else:
 print("\t\tVaccines not available")
 sys.exit()
def registration():
 global name,aadhar,mobno,dob,gender,ino
 fp1=open("register.dat","ab+")
 print("\n\t\tRegistration for dose 1 started\n")
 name=input("Enter Name :")
 aadhar=int(input("Enter Aadhar No. :"))
 mobno=int(input("Enter Mobile No. :"))
 dob=int(input("Enter date of birth(ddmmyyyy) :"))
 gender=input("Enter Gender(M/F) :")
 ino=dob+mobno
 print("\nRegistration ID :",ino,"\n")
 l1=[name,aadhar,mobno,dob,gender,ino]
 pickle.dump(l1,fp1)
 try:
 reader1=pickle.load(fp1)
 except:
 fp1.close()
def vaccenter():
 global ch2,choice
 fp2=open("center.dat","ab+")
 print("Vaccination Center Available Nearby ................\n")
 print("1. St. Vilnius Govt. Hospital")
 print("2. Anandiben Charity Trust Hospital")
 print("3. Khelvari Sr Sec School")
 print("4. Shramshakti Anganwari")
 print("5. Primary Health Centre")
 ch2=int(input("Enter your choice :"))
 if ch2==1:
 choice=" St. Vilnius Govt. Hospital"
 print("\nYour Vaccination Center is :",choice,"\n")
 elif ch2==2:
 choice="Anandiben Charity Trust Hospital"
 print("\nYour Vaccination Center is :",choice,"\n")
 elif ch2==3:
 choice="Khelvari Sr Sec School"
 print("\nYour Vaccination Center is :",choice,"\n")
 elif ch2==4:
 choice="Shramshakti Anganwari"
 print("\nYour Vaccination Center is :",choice,"\n")
 elif ch2==5:
 choice="Primary Health Centre"
 print("\nYour Vaccination Center is :",choice,"\n")
 l2=[choice]
 pickle.dump(l2,fp2)
 try:
 reader2=pickle.load(fp2)
 except:
 fp2.close()
def vacdate():
 global ch3,choice2
 fp3=open("date.dat","ab+")
 print("Available date slots of this month :\n")
 print("1. 1-8\n2. 9-15\n3. 16-22\n4. 22-31")
 ch3=int(input("Enter your choice"))
 if ch3==1:
 choice2="1-8"
 print("\nYour Date Slot is :",choice2,"\n")
 elif ch3==2:
 choice2="9-15"
 print("\nYour Date Slot is :",choice2,"\n")
 elif ch3==3:
 choice2="16-22"
 print("\nYour Date Slot is :",choice2,"\n")
 elif ch3==4:
 choice2="23-31"
 print("\nYour Date Slot is :",choice2,"\n")
 l3=[choice2]
 pickle.dump(l3,fp3)
 try:
 reader3=pickle.load(fp3)
 except:
 fp3.close()
print()
print()
print(" JABALPUR COVID CONTROL CELL ")
print("-----------------------------------------------------------------------------")
print(" Department of Health (JMC) ")
print()
print()
print("\t\t\t\tCovid Mantra\n")
print("\t\t1. Wear a mask")
print("\t\t2. Social Distancing")
print("\t\t3. Hand Sanitiser")
print("-----------------------------------------------------------------------------")
while True:
 print()
 print()
 print("\t\tMain Menu\n")
 print("1. Administration Department")
 print("2. User Menu")
 print("3. Exit")
 ch=int(input("Enter your choice : "))
 print()
 if ch==1:
 print("\t\t\tAdministration Department\n")
 print("a. Insertion of Hospital Record ")
 print("b. Statistics")
 choice=input("Enter your choice : ")
 print()
 if choice=="a":
 print("\t\tInsertion of Hospital Record\n")
 addhos()
 print("Hospital added successfully")
 print("---------------------------------------------------------------------------")
 elif choice=="b":
 print("\t\tStatistics\n")
 stats = PrettyTable(["Serial No.", "Subject", "Data"])
 stats.add_row(["1", "Active Cases", random.randint(100000, 200000)])
 stats.add_row(["2", "Positivity Rate (India) ", random.randrange(4,10)])
 stats.add_row(["3", "Positivity Rate (Jabalpur) ", random.randrange(3,10)])
 stats.add_row(["4", "Recovery Percentage", random.randrange(75,100)])
 stats.add_row(["5", "Total Deaths", random.randint(100000, 150000)])
 stats.add_row(["6", "Total Vaccinations", random.randint(1000000, 1500000)])
 print(stats)
 print("---------------------------------------------------------------------------")
 elif ch==2:
 print("\t\t\tUser Menu\n")
 print("A. Check Hospital Availability")
 print("B. Vaccination Registration")
 print("C. Vaccination Certificate")
 print("D. Feedback")
 choice1=input("Enter your choice : ")
 print()
 if choice1=="A":
 print("\t\t\t\tHospital Available\n")
 hoslist()
 print()
 cod = int(input("Please enter code of your prefered hospital : "))
 repeat = int(input("Enter No. of patients : "))
 amount = (repeat * 200)
 for i in range(0, repeat):
 a = input("Enter Full Name of Patient : ")
 b = input("Enter Age of Patient : ")
 c = input("Enter Gender of Patient : ")
 d = input("Any symptoms of COVID-19 in last 7 days(y/n) : ")
 if d == "y":
 dsub = input("Please enter symptoms in short (Snezzing , loss of smell/taste
, etc):")
 else:
 print()
 e = input("Any pre-existing chronic disease/medical complication:")
 f = int(input("Enter a valid phone number:"))
 print()
 print("--------Payment Tab--------")
 gst = 100
 ser = 50
 total = (amount + gst + ser)
 y=PrettyTable()
 y.field_names=["S.No", "Item", "Amount"]
 y.add_row(["0", "Bill per patient", "$200"])
 y.add_row(["1","No. of patients",repeat])
 y.add_row(["2", "Hospital Fee", amount])
 y.add_row(["3", "GST", gst])
 y.add_row(["4", "Service Tax", ser])
 y.add_row(["5", "Grand Total", total])
 print()
 m = input("Press y to confirm and proceed to payment")
 print()
 print("Total Payable amount: ", total)
 print()
 pay()
 print("------------------------------------------------------------------------")
 elif choice1=="B":
 print("\t\tVaccination Registration\n")
 print("Vaccination slot booking")
 print("D1. Dose 1 ")
 print("D2. Dose 2 ")
 ch1=input("Enter your choice : ")
 print()
 fp4=open("slotdose1.dat","ab+")
 if ch1=="D1":
 print("\tSlot Booking for Dose 1")
 dose()
 registration()
 vaccenter()
 vacdate()
 print("\t\tRegistration Successful\n")
 x=PrettyTable()
 x.field_names=["Aadhar No.","Name","Dose","District","Vaccination
center","Date slot"]
 x.add_row([aadhar,name,"1",dist,choice,choice2])
 print(x)
 l4=x.get_string()
 pickle.dump(l4,fp4)
 try:
 reader4=pickle.load(fp4)
 except:
 fp4.close()
 fp5=open("slotdose2.dat","ab+")
 if ch1=="D2":
 print("\tSlot Booking for Dose 2")
 regid=input("Enter your registration id : ")
 aadharno=int(input("Enter your Aadhar Card no. :"))
 dateob=int(input("Enter your date of birth(ddmmyy) : "))
 print("\n")
 vacdate()
 y=PrettyTable()
 y.field_names=["Aadhar No.","DOB","Dose","Date slot"]
 y.add_row([aadharno,dateob,"2",choice2])
 print(y)
 l5=y.get_string()
 pickle.dump(l5,fp5)
 try:
 reader5=pickle.load(fp5)
 except:
 fp5.close()
 print("-----------------------------------------------------------------------------")
 elif choice1=="C":
 print("\t\tVaccination certificate")
 register_id=int(input("Enter registration Id : "))
 aadhar_no=int(input("Enter aadhar no. : "))
 name_=input("Enter your name : ")
 age_=int(input("Enter your age : "))
 d_o_b=int(input("Enter your date of birth(ddmmyyyy) : "))
 gender_=input("Enter your gender (M/F/O) : ")
 vacname=["Covishield","Covaxin"]
 vac_name=random.choice(vacname)
 vacby=["Nisha Pandey","Alkaa Mallik","Tarun Khosla","Karan Mehran","Anjum
Sharma","Soham Sherpa","Rohan Khanna","Priya Kapoor","Amrit Shegal","Rajiv
Neelam","Monik Viveka"]
 vac_by=random.choice(vacby)
 vacat=["Primary Health Center","St. Peter Hospital","Ravindra
Hospital","Aarogya Hospital","Seven Hills Hospital","Cooper Municipal Hospital","VM
Desai Hospital"]
 vac_at=random.choice(vacat)
 vacdate=["05-08-2021","12-09-2021","22-09-2021","18-08-2021"]
 vac_date=random.choice(vacdate)
 print("\n")
 print("+---------------------------------------------------------------+")
 print("|\t\tMinistry of Health & Family Welfare\t\t|")
 print("|\t\t\tGovernment of India\t\t\t|")
 print("|\t\t\t\t\t\t\t\t|")
 print("|\tProvisional Certificate for COVID-19 Vaccination\t|")
 print("| |")
 print("|Beneficiary Details\t\t\t\t\t\t|")
 print("|Name \t\t\t",name_,"\t\t\t\t|")
 print("|Age \t\t\t",age_,"\t\t\t\t\t|")
 print("|Gender \t\t",gender_,"\t\t\t\t\t|")
 print("|Aadhar No. :\t\t",aadhar_no,"\t\t\t\t|")
 print("|Registration id :\t",register_id,"\t\t\t\t|")
 print("| |")
 print("|\t------------------------------------------------ \t|")
 print("| |")
 print("|Vaccination Details","\t\t\t\t\t\t|")
 print("|Vaccine Name\t\t",vac_name,"\t\t\t\t|")
 print("|Date of Vaccination\t",vac_date,"\t\t\t\t|")
 print("|Vaccinated by\t\t",vac_by,"\t\t\t\t|")
 print("|Vaccinated at\t\t",vac_at,"\t\t\t|")
 print("+---------------------------------------------------------------+")
 elif choice1=="D":
 feed=input("Enter your feedback : ")
 print("Thank You for your feedback\n")
 print("---------------------------------------------------------------------------")
 exit()
 else:
 exit()