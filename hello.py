import os
import getpass

os.system("tput setaf 1")
print("\t\t\tTERMINAL USER INTERFACE")
os.system("tput setaf 7")

print("\t\t\t------------------------")

passwd = getpass.getpass("Enter the password: ")
apass = "mb"

if passwd != apass:
	print("Access Denied")
	exit()

print("Where you would like to perform your job(local/remote)?",end=' ')
location = input()
print(location)

if location == "remote":
	remoteIP = input("Enter the IP Address: ")

while True:
	print("""
Press 1: Find Date
Press 2: Check Calender
Press 3: Configure Web Server
Press 4: Create a new User
Press 5: Create File
Press 6: Create a Network
Press 7: Check if a Software is present
Press 8: Exit
	""")

	print("Enter Your Choice: ",end=' ')
	ch = input()

	if location == "local":
		if int(ch) == 1:
			os.system("date")
		elif int(ch) == 2:
			os.system("cal")
		elif int(ch) == 3:
			os.system("yum install httpd")
		elif int(ch) == 4:
			print("Enter the UserName: ",end=' ')
			userName = input()
			os.system("useradd {}".format(userName))
		elif int(ch) == 5:
			print("Enter The File Name: ",end=' ')
			file_name = input()
			os.system("mkdir {}".format(file_name))
		elif int(ch) == 6:
			os.system("date")
		elif int(ch) == 7:
			print("Enter the Software Name: ",end=' ')
			software_name = input() 
			os.system("rpm -q {}".format(software_name))
		elif int(ch) == 8:
			exit()
		else: 	
			print("Invalid Choice!!")
		input("Enter to continue...")	
		os.system("clear")

	elif location == "remote":
		if int(ch) == 1:
			os.system("ssh {0} date".format(remoteIP))
		elif int(ch) == 2:
			os.system("ssh {0} cal".format(remoteIP))
		elif int(ch) == 3:				
			os.system("yum install httpd")
		elif int(ch) == 4:
			print("Enter the UserName: ",end=' ')
			userName = input()
			os.system("ssh {0} useradd {1}".format(remoteIP,userName))
		elif int(ch) == 5:
			print("Enter The File Name: ",end=' ')
			file_name = input()
			os.system("mkdir {}".format(file_name))
		elif int(ch) == 6:
			os.system("date")
		elif int(ch) == 7:
			print("Enter the Software Name: ",end=' ')
			software_name = input() 
			os.system("rpm -q {}".format(software_name))
		elif int(ch) == 8:
			exit()
		else: 	
			print("Invalid Choice!!")

	else:
		print("Location not supported!!")











