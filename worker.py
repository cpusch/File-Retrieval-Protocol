import socket
import sys



SPLIT_SIZE = 1000
localIP = sys.argv[1]
localPort   = 60000
bufferSize  = 1024

# Create a datagram socket
UDPWorkerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPWorkerSocket.bind((localIP, localPort))

print(f"{localIP} waiting to work")

# Listen for incoming datagrams
while(True):
    bytesAddressPair = UDPWorkerSocket.recvfrom(bufferSize)
    serverMessage = bytesAddressPair[0]
    serverAddress = bytesAddressPair[1]

    clientMsg = str(serverMessage.decode())
    clientIP  = "Client IP Address:{}".format(serverAddress)
    with open(f'./files/{clientMsg}','rb') as file:
        file_bytes = file.read()

    byte_array = [file_bytes[i:i+SPLIT_SIZE] for i in range(0, len(file_bytes), SPLIT_SIZE)]


    # print(clientMsg)
    print(clientIP)

    # Sending a reply to client
    for i,bytes in enumerate(byte_array):
        if i == (len(byte_array) - 1):
            UDPWorkerSocket.sendto(b'LAS'+bytes, serverAddress)
        else: 
            UDPWorkerSocket.sendto(b'MOR'+bytes, serverAddress)
        
