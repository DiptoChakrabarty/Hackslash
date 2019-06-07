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
		sp.getoutput("ansible-playbook /root/Desktop/Linux\ World/Menu-Optimization/add_user.yml")
	if cmd=="dockerlaunch":
		sp.getoutput("ansible-playbook /root/Desktop/Linux\ World/Menu-Optimization/Dockers/docker_start.yml")
	if cmd=="httpd":
		sp.getoutput("ansible-playbook /root/Desktop/Linux\ World/Menu-Optimization/Web/httpd_launch.yml")
	if cmd=="nginx":
		sp.getoutput("ansible-playbook /root/Desktop/Linux\ World/Menu-Optimization/Web/nginx.yml")
 
	if cmd=="exit":
		break


