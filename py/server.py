import socket
import RPi.GPIO as GPIO

host = '192.168.0.112'
port = 5560
led_pin = 8

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created')
    try:
        s.bind((host,port))
    except socket.error as msg:
        print(msg)
    print('Socket bind complete')
    return s

def setupConnection():
    s.listen(1)
    conn, address = s.accept()
    print('Connected to' + address[0] + ':' + str(address[1]))
    return conn

def ON_LED():
    reply = 'LED ON'
    GPIO.output(led_pin, True)
    return reply

def OFF_LED():
    reply = 'LED OFF'
    GPIO.output(led_pin, False)
    return reply
def dataTransfer(conn):
    while True:
        data = conn.recv(1024)
        data = data.decode('utf-8')
        command = data
        
        if command == 'ON':
            reply = ON_LED()
        elif command == 'OFF':
            reply = OFF_LED()
        elif command == 'KILL':
            print('Server is shutting down')
            s.close()
            break
        else:
            reply = 'Unknown command'
        conn.sendall(str.encode(reply))
        print('Data has been sent!')
    conn.close()
    GPIO.cleanup()
s= setupServer()
while True:
    try:
        conn = setupConnection()
        dataTransfer(conn)
    except:
        break
            
