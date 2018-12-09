# Description: Script used to unzip (.zip) files from a databases


import os
count = 0
for (dirname, dirs, files) in os.walk('.'):
   for filename in files:
       if filename.endswith('.txt') :
           count = count + 1
print 'Files:', count

python txtcount.py

# import subprocess
# import sys
#
# HOST="chaos.cs.uchicago.edu"
# # Ports are handled in ~/.ssh/config since we use OpenSSH
# COMMAND="uname -a"
#
# ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
#                        shell=False,
#                        stdout=subprocess.PIPE,
#                        stderr=subprocess.PIPE)
# result = ssh.stdout.readlines()
# if result == []:
#     error = ssh.stderr.readlines()
#     print >>sys.stderr, "ERROR: %s" % error
# else:
#     print result


# import spur
#
# shell = spur.SshShell(hostname="chaos.cs.uchicago.edu", username="tylernass", password="Gorregated814$")
# result = shell.run(["cd", "/tartarus"])
# # cd /tartarus/tylernass
# print(result.output) # prints hello


# from pexpect import pxssh
# s = pxssh.pxssh()
# if not s.login ('chaos.cs.uchicago.edu', 'tylernass', 'Gorregated814$'):
#     print("SSH session failed on login.")
#     print(str(s))
# else:
#     print("SSH session login successful")
#     s.sendline ('ls -l')
#     s.prompt()
#     print(s.before)     # print everything before the prompt.
#     s.logout()


# 1: Logon to server
#
# import paramiko
# client=paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect('chaos.cs.uchicago.edu', username='tylernass')
# grepCommand="ssh  username@hostname"
# stdin,stdout,stderr = client.exec_command(grepCommand)
# data=stdout.readlines()
# print data
# client.close()


# import pxssh
# import getpass
# try:
#     s = pxssh.pxssh()
#     hostname = chaos.cs.uchicago.edu
#     username = tylernass
#     password = Gorregated814$
#     s.login (hostname, username, password)
#     s.sendline ('uptime')   # run a command
#     s.prompt()             # match the prompt
#     print s.before          # print everything before the prompt.
#     s.sendline ('ls -l')
#     s.prompt()
#     print s.before
#     s.sendline ('df')
#     s.prompt()
#     print s.before
#     s.logout()
# except pxssh.ExceptionPxssh, e:
#     print "pxssh failed on login."
#     print str(e)
