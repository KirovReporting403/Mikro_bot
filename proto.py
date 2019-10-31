import paramiko,time,telebot,os,re

k = paramiko.RSAKey.from_private_key_file("/home/humanz/ssh/backup/mikrotik.pem")
client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.load_host_keys('/home/humanz/.ssh/known_hosts')
client.connect('7cbd0896897a.sn.mynetname.net', username='Humanz',pkey = k, port=8090)
stdin, stdout, stderr = client.exec_command("/system script run dhclient")
result = stdout.read().decode('utf-8').strip("\n")
print(result)
