def data_recv():
	data=cl.recv(50)
	cmd=data.decode()
	return cmd
def data_send(cmd):
	s.send(cmd.encode())
def ip_add(ip,user,passwd):
	sp.getoutput(" echo {} | cat >> hosts".format(ip))
	sp.getoutput(" ssh-copy-id -p {}  {}@{}".format(passwd,user,ip))
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
		print(ip)
		user=data_recv()
		print(user)
		passwd=data_recv()
		print(passwd)
		if ip!="localhost":
			ip_add(ip,user,passwd)
		os.system("ansible-playbook  ./Playbooks/add_user.yml --extra-vars  'var1={}' --extra-vars 'var0={}' ".format(username,ip))
	elif cmd=="exit":
		break

exit()
		
	

	
