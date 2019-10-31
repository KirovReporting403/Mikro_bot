import paramiko,time,telebot,os,re

k = paramiko.RSAKey.from_private_key_file("<<--Your RSA key-->>")
client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.load_host_keys('<<--Your Know Host-->>')
client.connect('<<--IP address or domain-->>', username='<<--mikrotik username-->>,pkey = k, port=<<--mikrotik port-->>)
stdin, stdout, stderr = client.exec_command("/system script run <<-- name of script[dhcp client/info/ip public] -->>")
result = stdout.read().decode('utf-8').strip("\n")
print(result)
client.close()
