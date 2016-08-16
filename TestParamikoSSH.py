#!/usr/bin/python3
import socket
import paramiko

host = ''
username = ''
password = ''
port = 22

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(host, username=username, password=password, port=port)
    connected = True
except paramiko.SSHException:
    print('Error connecting to host (%s)' % host)
    print('Host is not a valid SSH server\nUsername is not valid or incorrect password')
except paramiko.ssh_exception.NoValidConnectionsError:
    print('Connection Failed')
    quit()
except socket.gaierror:
    print('Socket not being to resolve the address (%s)' % host)
except TimeoutError:
    print('The (%s) host didn\'t respond' % host)
    quit()

stdin,stdout,stderr = ssh.exec_command("ls /etc/")

for line in stdout.readlines():
    print(line.strip())
ssh.close()