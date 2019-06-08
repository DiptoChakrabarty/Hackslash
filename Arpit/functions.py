import os
def local_webserver():
	os.system("echo '[web]' | cat > /root/Menu/hosts")
	os.system("echo '127.0.0.1 ansible_user=root ansible_password=redhat' | cat >> /root/Menu/hosts")
	os.system("ansible-playbook webserver.yml")

def remote_webserver():
	import os
	ip_no=input("Enter no of ip's where you want to perform this task")
	os.system("echo '[web]' | cat > /root/Menu/hosts")
	for i in range(int(ip_no)):
		ip=input("Enter ip of remote")
		username=input("Enter username with whom you want to be performed this task")
		password=input("Enter password of given user")
		os.system("sshpass -p {} ssh-copy-id {}@{}".format(password,username,ip))
		os.system("echo '{} ansible_user={} ansible_password={}' | cat >> /root/Menu/hosts".format(ip,username,password))
	os.system("ansible-playbook webserver.yml")

def local_docker():
	os.system("echo '[docker]' | cat > /root/Menu/hosts")
	os.system("echo '127.0.0.1 ansible_user=root ansible_password=redhat' | cat >> /root/Menu/hosts")
	#run_playbook for installing docker and starting service
	doc_in=int(input("Enter no of docker would you want to launch"))
	l=[]
	for i in range(doc_in):
		l.append(input("enter name of {} docker container".format(i+1)))
	for i in l:	
		os.system("ansible-playbook launch_container.yml -e '{}' ".format(i))
	#run playbook for launching docker in different terminal with set hostname

def remote_docker():
	pass

def mail():
	mail_id=input("Enter your mail id")
	password_=input("Enter your password")
	send_to=input("enter mail where to send")
	subject=input("enter input")
	body=input("Enter body content")
	os.system("ansible-playbook mail.yml -e 'mail_id={} mail_passwd={} send_to={} subject={} body={}'")
	
