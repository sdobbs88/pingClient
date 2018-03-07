from datetime import datetime
from socket import *

def main():
    
    serverName = 'localhost'
    serverPort = 1853
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    message = 'Ping'.encode()
    
    counter = 10
    i = 0
    
    print ('Now attempting ', counter, ' pings...\n')
    
    while i < counter:
        
        i+= 1
        print ('This is Ping Attempt Number: ', i)
        print ('There are ', counter - i, ' attempts left.')
        
        a = datetime.now()
        clientSocket.sendto(message,(serverName, serverPort))
        
        clientSocket.settimeout(1)
        
        try:
            modifiedMessage,serverAddress = clientSocket.recvfrom(1024)
        
            b = datetime.now()
            c = a - b;
            print ('A----> ',a)
            print ('B----> ',b)

            print ('Elapsed time in microseconds is: ', c.microseconds,'\n')
        except timeout:
            print ('Sorry! The connection has timed out. Please try again.\n')
            
    if i == 10:
        print ('Exiting')
        clientSocket.close()
        print ('Socket has been closed. No more pings')
    
    pass

if __name__ == "__main__":
    main()
