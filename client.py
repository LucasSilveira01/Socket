import socket
def client(host = 'localhost', port=10000): 
    # Create a TCP/IP socket 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # Connect the socket to the server 
    server_address = (host, port) 
    sock.connect(server_address) 
    # Send data 
    try: 
        # Send data 
        message = "2022-03-01,16:21:30,16:21:40" 
        print ("Sending %s" % message) 
        sock.sendall(message.encode('utf-8')) 
    finally: 
        print ("Closing connection to the server") 
        sock.close() 
client()