import socket
import os
import subprocess as sp
while True:
	cmd=input("Enter Command")
	if cmd=="adduser":
		username=input("Enter Username ")
		sp.getoutput("ansible-playbook /root/Desktop/Linux\ World/Menu-Optimization/add_user.yml")
		sp.getoutput("echo ${}".format(username))
	if cmd=="dockerlaunch":
		sp.getoutput("ansible-playbook /root/Desktop/Linux\ World/Menu-Optimization/Dockers/docker_start.yml")
	if cmd=="httpd":
		sp.getoutput("ansible-playbook /root/Desktop/Linux\ World/Menu-Optimization/Web/httpd_launch.yml")
	if cmd=="nginx":
		sp.getoutput("ansible-playbook /root/Desktop/Linux\ World/Menu-Optimization/Web/nginx.yml")
 
	if cmd=="exit":
		break


