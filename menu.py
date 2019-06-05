print("\t\tWelcome to your virtual asistant")
print("\t\t--------------------------------\n")

while True:
	print("\t\tpress1 to configure webserver")
	print("\t\tpress2 to launch ec2 instance")
	print("\t\tpress3 to start your privacy in computer")
	print("\t\tpress4 to launch docker")
	print("\t\tpress5 to run command manually on remote server")

	choice=int(input("Enter your choice"))	

	if choice==1:
		value=input("Where do you want to perform thi task local/remote")
		if value=='local':
			pass
		elif value=='remote':
			ip=input("Enter ip where you want to perform this task")
			username=input("Enter username with whom you want to be performed this task")
			password=input("Enter password of given user")
			import os
			os.system("sed -i 's/hosts:/hosts: {}/' /root/Menu/webserver.yml".format(ip))
			os.system("echo '{} ansible_user={} ansible_password={} StrictHostChecking=no' | cat >> /etc/ansible/hosts".format(ip,username,password))
			os.system("ansible-playbook webserver.yml")

		else:
			print("Please enter valid choice")

	else:
		print("invalid")
	choice_con=input("Do you want to continue y/n")
	if choice_con=='n':
		break