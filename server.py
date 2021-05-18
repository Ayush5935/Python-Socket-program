import socket


s = socket.socket()
print("Socket Created")

s.bind(("localhost",600))

s.listen(3)
print("Waiting For Connection")


while True:
    c,addr = s.accept()
    name = c.recv(1024).decode()

    print("connected with",addr,name)

    c.send(bytes("Hiii it's me Ayush" , "utf-8"))

    c.close()