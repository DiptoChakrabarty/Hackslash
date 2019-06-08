#!/usr/bin/python36
import os
import functions

while True:
	print("\t\tWelcome to your virtual asistant")
	print("\t\t--------------------------------\n")
	print("\t\tpress1 to configure webserver")
	print("\t\tpress2 to run docker")
	print("\t\tpress3 to send mail ")
	print("\t\tpress4 to take software as a service ")
	print("\t\tpress4 to launch ec2 instance")
	print("\t\tpress5 to run command manually on remote server")

	choice=int(input("Enter your choice"))	

	if choice==1:
		value=input("Where do you want to perform thi task local/remote")
		if value=='local':
			functions.local_webserver()
		elif value=='remote':
			functions.remote_webserver()
		else:
			print("Please enter valid choice")

	if choice==2:
		value=input("Where do you want to perform this task local/remote")
		if value=='local':
			functions.local_docker()
		elif value=='remote':
			functions.remote_docker()
		else:
			print("Please enter valid choice")
	if choice==3:
		functions.mail()

	else:
		print("invalid")
	choice_con=input("Do you want to continue y/n")
	if choice_con=='n':
		break