def root():
	import subprocess as sp 
	import os
	a=sp.getoutput("cat /etc/shadow | grep root")

	a=a.split(':')
	a=a[1]

	while True:
		var=sp.getoutput("cat /etc/shadow | grep root")
		
		var=var.split(':')
		var1=var[1]
		try:

			if var1!=a:
				os.system("echo 'arpit' | passwd root --stdin ")
				os.system("loginctl lock-session")
				break
				import send_sms
				send_sms.sms()
				import mail
				mail.mail()
				os.system("cal > /dev/pts/0")

				root()

			elif var1==a:
				pass
		except:
			pass
root()
