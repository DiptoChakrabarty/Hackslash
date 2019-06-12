<<<<<<< HEAD
=======
def data_recv():
	data=cl.recv(50)
	cmd=data.decode()
	return cmd
def data_send(cmd):
	s.send(cmd.encode())
def ip_add(ip,user,passwd):
	sp.getoutput(" echo '[current]' | cat > hosts ")
	sp.getoutput(" echo {} | cat >> hosts".format(ip))
	sp.getoutput(" ssh-copy-id -p {}  {}@{}".format(passwd,user,ip))
def ip_check(ip):
	if ip!="localhost":
		user=data_recv()	
		passwd=data_recv()
		ip_add(ip,user,passwd)
import socket
import os
import subprocess as sp
s=socket.socket()
port = 1452
ip= "192.168.43.254"
s.bind((ip,port))
s.listen()
cl,addr=s.accept()

while True:
	cmd=data_recv()
	print(cmd)
	if cmd=="adduser":
		username=data_recv()
		print(username)
		ip=data_recv()
		ip_check(ip)
		os.system("ansible-playbook  ./Playbooks/add_user.yml --extra-vars  'var1={}' --extra-vars 'var0={}' ".format(username,ip))
	elif cmd=="yum":
		ip=data_recv()
		ip_check(ip)
		os.system("ansible-playbook  ./Playbooks/systems/repolist.yml --extra-vars 'var0={}' ".format(ip))
	elif cmd=="webserver":
		server=data_recv()
		ip=data_recv()
		ip_check(ip)
	#	os.system("ansible-playbook  ./Playbooks/systems/repolist.yml --extra-vars 'var0={}' ".format(ip))
		os.system("ansible-playbook  ./Playbooks/Web/{}.yml".format(server))
	elif cmd=="exit":
		break

	
		
	

	
>>>>>>> 8dcee1b987d12fd46e35536c1bfbd69fc6e48100
