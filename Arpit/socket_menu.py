def get_remote_data():
	socket_send("enter remote ip")
	ip = socket_recv1()
	socket_send("enter username with whom you want to perform this task")
	username=socket_recv1()
	socket_send("Enter password of {} user".format(username))
	password=socket_recv1()	
	
	return [ip,username,password]

def socket_send(data):
	data=data.encode()
	session.send(data)	
def socket_recv1():
	data=session.recv(1024)
	data=data.decode()
	return data

import subprocess as sp 
import socket
import socket_functions
s=socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port=1234
ip='192.168.43.217'


s.bind((ip,port))
s.listen()

session,addr=s.accept()

while True:

	cmd=socket_recv1()

	if cmd=='1':	
		socket_send("where do you want to perform  local/remote")
		out=socket_recv1()
		if out=='local':
			socket_functions.local_webserver()
			session.send(b"successfully configured webserver")
		elif out=='remote':
			ip,username,password=get_remote_data()
			socket_functions.remote_webserver(ip,username,password)
			session.send(b"successfully configured webserver at remotely")
	elif cmd=='2':
		socket_send("where do you want to perform  local/remote")
		out=socket_recv1()
		if out=='local':
			socket_send("enter no of docker would you want to launch")
			doc_no = socket_recv1()
			doc_name=[]
			for i in range(int(doc_no)):
				socket_send("enter docker {} name".format(i+1))
				name=socket_recv1()
				doc_name.append(name)
			socket_functions.local_docker(doc_no,doc_name)
			socket_send("successfully launched docker containers")


		elif out=='remote':
			ip,username,password=get_remote_data()
			socket_send("enter no of docker would you want to launch")
			doc_no = socket_recv1()
			doc_name=[]
			for i in range(int(doc_no)):
				socket_send("enter docker {} name".format(i+1))
				name=socket_recv1()
				doc_name.append(name)
			socket_functions.remote_docker(doc_no,doc_name,ip,username,password)
			socket_send("successfully launched docker containers")

	elif cmd=='3':
		socket_send("enter number where you want to send msg")
		phone_no=socket_recv1()
		socket_send("enter mesage would you want to send")
		message_twilio=socket_recv1()
		socket_functions.sms(phone_no,message_twilio)
		socket_send("successfully sent mesage")


	elif cmd=='4':
		socket_send("enter yout mail_id")
		mail_id_sender=socket_recv1()
		socket_send("enter your password")
		password=socket_recv1()
		socket_send("enter reciver mail_id")
		mail_id_reciever=socket_recv1()
		socket_send("enter subject")
		subject=socket_recv1()
		socket_send("enter body")
		body=socket_recv1()

		socket_functions.mail(mail_id_sender,password,mail_id_reciever,subject,body)
		socket_send("successfully sent mesage")

	elif cmd=='5':
		socket_send("which software would you want to launch")
		out=socket_recv1()
		if out=='firefox':
			os.system("python36 python_files/saas.py")
			socket_send("successfully launched firefox")
	elif cmd=='exit':
		break

	else:
		print(cmd)
		session.send(b"some error occured")


