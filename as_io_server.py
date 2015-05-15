### Tcp Chat server
## 
##import socket, select
## 
###Function to broadcast chat messages to all connected clients
##def broadcast_data (sock, message):
##    #Do not send the message to master socket and the client who has send us the message
##    for socket in CONNECTION_LIST:
##        if socket != server_socket and socket != sock :
##            try :
##                socket.send(message)
##            except :
##                # broken socket connection may be, chat client pressed ctrl+c for example
##                socket.close()
##                CONNECTION_LIST.remove(socket)
## 
##if __name__ == "__main__":
##     
##    # List to keep track of socket descriptors
##    CONNECTION_LIST = []
##    RECV_BUFFER = 1024 # Advisable to keep it as an exponent of 2
##    PORT =21582
##     
##    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##    # this has no effect, why ?
##    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
##    server_socket.bind(("192.168.8.143", PORT))
##    server_socket.listen(10)
## 
##    # Add server socket to the list of readable connections
##    CONNECTION_LIST.append(server_socket)
## 
##    print "Chat server started on port " + str(PORT)
## 
##    while 1:
##        # Get the list sockets which are ready to be read through select
##        read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
## 
##        for sock in read_sockets:
##            #New connection
##            if sock == server_socket:
##                # Handle the case in which there is a new connection recieved through server_socket
##                sockfd, addr = server_socket.accept()
##                CONNECTION_LIST.append(sockfd)
##                print "Client (%s, %s) connected" % addr
##                 
##                broadcast_data(sockfd, "[%s:%s] entered room\n" % addr)
##             
##            #Some incoming message from a client
##            else:
##                # Data recieved from client, process it
##                try:
##                    #In Windows, sometimes when a TCP program closes abruptly,
##                    # a "Connection reset by peer" exception will be thrown
##                    data = sock.recv(RECV_BUFFER)
##                    if data:
##                        broadcast_data(sock, "\r" + '<' + str(sock.getpeername()) + '> ' + data)                
##                 
##                except:
##                    broadcast_data(sock, "Client (%s, %s) is offline" % addr)
##                    print "Client (%s, %s) is offline" % addr
##                    sock.close()
##                    CONNECTION_LIST.remove(sock)
##                    continue
##     
##    server_socket.close()
#!/usr/bin/env python  
#!/usr/bin/env python  
#!/usr/bin/env python  
import socket,select  
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
##server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)  
server.bind(('192.168.8.143',21582))  
server.listen(5)  
inputs=[server]  
while 1:  
    rs,ws,es=select.select(inputs,[],[],1)  
    for r in rs:  
        if r is server:  
            clientsock,clientaddr=r.accept();  
            inputs.append(clientsock);
##            print inputs
            print "connected by",clientaddr
			print "welcome!"
			print "nihao"
        else:
           try: 
            data=r.recv(1024);  
            if not data:  
                inputs.remove(r);  
            else:  
                print data
                r.send('1')
           except:
               print "%s:close"%(clientaddr[0])
               r.close()
               inputs.remove(r)
               continue
server.close()
