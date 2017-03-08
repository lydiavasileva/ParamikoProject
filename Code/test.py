import paramiko
from paramiko import SSHClient
from scp import SCPClient

class SSHConnection:
	"""docstring for SCPConnection"""
	def __init__(self, ip, uName, uPass):
		self.ssh = SSHClient()
		self.ssh.load_system_host_keys()
		self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		self.ssh.connect(hostname=ip, port=22, username=uName, password=uPass)

	def getFile(self, srcDir, dstDir):
		self.scp = SCPClient(self.ssh.get_transport())

		self.scp.get(srcDir, dstDir)

		self.scp.close()

	def pushFile(self, srcDir, dstDir):
		self.scp = SCPClient(self.ssh.get_transport())

		self.scp.put(srcDir, dstDir)

		self.scp.close()

myConn = SSHConnection('10.210.14.132', 'root', 'juniper1')

#myConn.getFile('/config/juniper.conf.1.gz','/home/helweg/Dokumenter/ParamikoProject/conf1.test.gz')

myConn.pushFile('/home/helweg/Dokumenter/ParamikoProject/conf1.test.gz','/config/juniper.conf.test.gz')
