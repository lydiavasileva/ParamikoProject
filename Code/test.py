import paramiko
from paramiko import SSHClient
from scp import SCPClient

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='10.210.14.132', port=22, username="root", password="juniper1")
# SCPCLient takes a paramiko transport as its only argument
scp = SCPClient(ssh.get_transport())

#scp.get('/config/juniper.conf.1.gz', '/home/helweg/Dokumenter/ParamikoProject/conf1.1.gz')
scp.put('/home/helweg/Dokumenter/ParamikoProject/conf1.1.gz', '/config/juniper.conf.test.gz')

scp.close()
