import socket
import subprocess as sp
s=socket.socket()
port = 1324
ip= "192.168.43.254"
s.bind((ip,port))
s.listen()
cl,addr=s.accept()
while True:
	data=cl.recv(50)
	cmd=data.decode()
	cl.send(data)
	if cmd=="adduser":
		data2=cl.recv(20)
		username=data2.decode()
		sp.getoutput("ansible-playbook /root/Desktop/Github/Menu-Automation/add_user.yml --extra-vars 'var1={}'".format(username))
	if cmd=="dockerlaunch":
		data2=cl.recv(20)
		name=data2.decode()
		sp.getoutput("ansible-playbook /root/Desktop/Github/Menu-Automation/Dockers/docker_update.yml --extra-vars  'var1={}'".format(name))
	if cmd=="httpd":
		sp.getoutput("ansible-playbook /root/Desktop/Github/Menu-Automation/Web/httpd_launch.yml")
	if cmd=="nginx":
		sp.getoutput("ansible-playbook /root/Desktop/Github/Menu-Automation/Web/nginx.yml")
	if cmd=="mail":
		sp.getoutput("ansible-playbook /root/Desktop/root/Desktop/Github/Menu-Automation/Mail/mail_send.yml")
 
	if cmd=="exit":
		break


