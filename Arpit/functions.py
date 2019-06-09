import os
import subprocess
import getpass
def local_webserver():
	os.system("echo '[web]' | cat > hosts")
	os.system("echo '127.0.0.1 ansible_user=root ansible_password=redhat' | cat >> hosts")
	os.system("ansible-playbook playbooks/webserver.yml")

def remote_webserver():
	import os
	
	ip_no=input("Enter no of ip's where you want to perform this task")
	
	os.system("echo '[web]' | cat > hosts")
	
	for i in range(int(ip_no)):
		ip=input("Enter ip of remote")
		username=input("Enter username with whom you want to be performed this task")
		password=getpass.getpass("Enter password of given user")
		os.system("sshpass -p {} ssh-copy-id {}@{}".format(password,username,ip))
		os.system("echo '{} ansible_user={} ansible_password={}' | cat >> hosts".format(ip,username,password))
	
	os.system("ansible-playbook playbooks/webserver.yml")

def local_docker():
	os.system("echo '[docker]' | cat > hosts")
	os.system("echo '127.0.0.1 ansible_user=root ansible_password=redhat' | cat >> hosts")
	docker_no=input("Enter no of docker would you want to launch")
	
	for i in range(int(docker_no)):
		os.system("ansible-playbook playbooks/launch_container.yml")

def remote_docker():
	ip_no=input("Enter no of ip's where you want to perform this task")
	os.system("echo '[docker]' | cat > hosts")
	for i in range(int(ip_no)):
		ip=input("Enter ip of remote")
		username=input("Enter username with whom you want to be performed this task")
		password=input("Enter password of given user")
		os.system("sshpass -p {} ssh-copy-id {}@{}".format(password,username,ip))
		os.system("echo '{} ansible_user={} ansible_password={}' | cat >> hosts".format(ip,username,password))
		docker_no=input("Enter no of docker would you want to launch")
		for i in range(int(docker_no)):
			os.system("ansible-playbook playbooks/launch_container.yml")

def mail():
	os.system("ansible-playbook playbooks/mail.yml ")


def sms():
	os.system("ansible-playbook playbooks/message.yml")


def yum():
	ip_no=input("Enter no of ip's where you want to perform this task")
	os.system("echo '[yum]' | cat > hosts")
	for i in range(int(ip_no)):
		ip=input("Enter ip of remote")
		username=input("Enter username with whom you want to be performed this task")
		password=input("Enter password of given user")
		os.system("sshpass -p {} ssh-copy-id {}@{}".format(password,username,ip))
		os.system("echo '{} ansible_user={} ansible_password={}' | cat >> hosts".format(ip,username,password))
	os.system("ansible-playbook playbooks/yum.yml")