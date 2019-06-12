import os
import subprocess as sp

id_docker='firefox'

def launch_container():
	os.system(" docker run -itd --name {} --ipc=host -v /run/media/root/RHEL-7.5\ Server.x86_64:/dvd -v /root/rhel7_5_rpm_extras:/rpm -v /root/rhel7_extra_new_rpm:/new_rpm -v /root/python_lib:/python_lib -v /tmp/.X11-unix:/tmp/.X11-unix firefox:v2".format(id_docker))
	string='{print$2}'
	doc_ip=sp.getoutput("docker inspect {0} | grep -i ipaddress | sed -n '2 p' | awk {1} ".format(id_docker,string))
	print(doc_ip)
	doc_ip=doc_ip.split(':')
	doc_ip=doc_ip[1]
	doc_ip=doc_ip[:len(doc_ip)-1]
	print(doc_ip)
	return doc_ip
doc_ip=launch_container()


os.system("docker exec {} yum install firefox -y".format(id_docker))
os.system("gnome-terminal -x bash -c 'sshpass -p redhat  ssh -o StrictHostKeyChecking=no -X {} firefox; exec bash'".format(doc_ip))

