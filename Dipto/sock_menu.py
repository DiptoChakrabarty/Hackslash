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
	if cmd=="adduser":
		data2=cl.recv(20)
		username=data2.decode()
		sp.getoutput("ansible-playbook /root/Desktop/Github/Menu-Automation/add_user.yml --extra-vars 'var1={}'".format(username))
	if cmd=="dockerlaunch":
		data0=cl.recv(20)
		ip=data0.decode()
		data2=cl.recv(20)
		name=data2.decode()
		sp.getoutput("ansible-playbook /root/Desktop/Github/Menu-Automation/Dockers/docker_update.yml --extra-vars 'var0={}' --extra-vars  'var1={}'".format(ip,name))
	if cmd=="httpd":
		data0=cl.recv(20)
		ip=data0.decode()
		sp.getoutput("ansible-playbook /root/Desktop/Github/Menu-Automation/Web/httpd_launch.yml--extra-vars  'var0={}'".format(ip))
	if cmd=="nginx":
		data0=cl.recv(20)
		ip=data0.decode()
		sp.getoutput("ansible-playbook /root/Desktop/Github/Menu-Automation/Web/nginx.yml --extra-vars  'var0={}'".format(ip))
	if cmd=="mail":
		data0=cl.recv(50)
		ml=data0.decode()
		data1=cl.recv(20)
		at=data1.decode()	
		sp.getoutput("ansible-playbook /root/Desktop/root/Desktop/Github/Menu-Automation/Mail/mail_send.yml --extra-vars  'var0={}' --extra-vars 'var_attach={}'".format(ml,at))
	if cmd=="date":
		data0=cl.recv(20)
		ip=data0.decode()
		dt= sp.getoutput("date")
		cl.send(dt.encode())
	if cmd=="remoteadduser":
		data0=cl.recv(20)
		ip=data0.decode()
		data2=cl.recv(20)
		username=data2.decode()
		sp.getoutput("ansible-playbook /root/Desktop/Github/Menu-Automation/remote.yml --extra-vars  'var0={}' --extra-vars 'var1={}'".format(ip,username))
	if cmd=="sassfire":
		data0=cl.recv(20)
		host=data0.decode()
		data1=cl.recv(20)
		name=data1.decode()
		sp.getoutput("ansible-playbook /root/Desktop/Github/Menu-Automation/Dockers/docker.yml --extra-vars 'var0={}' --extra-vars 'var1={}'".format(host,name))
		sp.getoutput("ansible-playbook /root/Desktop/Github/Menu-Automation/Dockers/saas.yml  --extra-vars  'var0={}'".format(host)) 
	if cmd=="yum":
		data0=cl.recv(20)
		host=data0.decode()
		sp.getoutput("ansible-playbook /root/Desktop/Github/Menu-Automation/systems/repolist.yml --extra-vars  'var0={}'".format(host))
	if cmd=="exit":
		break


