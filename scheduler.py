#William Giddins Scheduler
import socket
from collections import deque


class Process: 
    def __init__(self, line):
        self.line = line.split(',')
        self.arrival_time = int(self.line[0])
        self.name = self.line[1]
        self.id = int(self.line[2])
        self.state = self.line[3]
        self.priority = int(self.line[4])
        self.interrupt = int(self.line[5])
        self.estimated_time = int(self.line[6])
        self.remaining_time = int(self.line[7])
        self.exec_time = int(self.line[8])
        
    
    def __str__(self):
        return ','.join(self.line)

    def __repr__(self):
        return str(self.id)


def connect(host, port):
    processes = deque([]) 
    PCB = deque([])
    total_elapsed = 11
    
    alg = input("What Algorithm will you use i.e FCFS, RR RCFS \n")


    with open('processes3.txt', 'r') as infile:
        
        for x in infile:
            processes.append(Process(x.strip('\n')))
        
        PCB.append(processes[0])
      
        i = 1


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))

        while len(PCB) > 0: 
            if (i < 14 and processes[i].arrival_time < total_elapsed):
               PCB.append(processes[i])
               i=i+1
            
            
            if (alg == 'FCFS'):
               PCB = deque(sorted(PCB, key=lambda x:x.arrival_time))
            elif (alg == 'RR FCFS'):
                 pass
            elif (alg == 'SJN'):
                  PCB = deque(sorted(PCB, key=lambda x:x.estimated_time))
            elif (alg == 'Priority'):
                 PCB = deque(sorted(PCB, key=lambda x:x.priority))
            elif (alg == 'RR SRTN'):
                 PCB = deque(sorted(PCB, key=lambda x:x.remaining_time))
            elif (alg == 'RR Priority'):
                  PCB = deque(sorted(PCB, key=lambda x:x.priority))
           
                 
            
            
            
            
            sock.send(str(PCB[0]).encode('utf-8'))
            PCB.popleft()				

            data = sock.recv(1024).decode()
            next_p = Process(data) 			
            if (next_p.remaining_time > 0):

                total_elapsed = total_elapsed + 20 #context switch 
                PCB.append(next_p)
                
            else:
                total_elapsed = total_elapsed + next_p.estimated_time
                wait_time = total_elapsed - next_p.arrival_time - next_p.exec_time			
                print('\tScheduler: Process %s, %s Completed ,Wait Time %s, Total Time Elapsed %s' % (next_p.id, next_p.name,wait_time, total_elapsed))
                
                


if __name__ == '__main__':

    host = '127.0.0.1'
    port = 9000

    connect(host, port)
