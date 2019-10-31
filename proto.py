import paramiko,time,telebot,os,re

k = paramiko.RSAKey.from_private_key_file("<<--Your RSA key-->>")
client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.load_host_keys('<<--Your Know Host-->>')
client.connect('<<--IP address or domain-->>', username='Humanz',pkey = k, port=8090)
stdin, stdout, stderr = client.exec_command("/system script run dhclient")
result = stdout.read().decode('utf-8').strip("\n")
print(result)
