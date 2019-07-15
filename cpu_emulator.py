#William Giddins CPU Emulator 
import socket





def listen(host, port):
    time_quantum = int(input("What is the time quantum?\n"),10) 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, port))
        sock.listen()

        print('Listening on %s:%s' % (host, port))

        conn, addr = sock.accept()

        with conn:
            print('Connection from:', addr,'\n')
            time_quantum = int(input("What is the time quantum?\n"),10)
            while True:
                data = conn.recv(1024)

                if not data:
                    break
                else:
                    data = data.decode()	
                    print('CPU Exec %s' % data) 
                    data = data.split(',')
                    data[-2] = str(int(data[-2]) - time_quantum) 
                    data[-1] = str(int(data[-1]) + time_quantum) #exec time
                    data = ','.join(data)	
                    conn.send(data.encode('utf-8')) 

            print('\nConnection closed to:', addr)


if __name__ == '__main__':

    host = '127.0.0.1'
    port = 9000

    listen(host, port)
