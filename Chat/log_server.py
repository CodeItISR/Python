import os
import socket
import threading

"""
    This is a multi socket server based on schedular and not threading.
    The function get_ip works on unix based os.
"""

PORT = 20001
FILE_PATH = 'log.txt'

acquire_print = threading.Lock()

def get_ip():

        """ Take the ip using Linux shell commands - wlan(wifi) connection"""
        
	f = os.popen('ifconfig wlan0 | grep "inet addr" | cut -f 2 -d ":" | cut -f 1 -d " "')
	ip = f.read()
	f.close()
	return ip

def log_info(conn, addr):

        """ For each connection get the error message and save it to the log.txt file """
        
	global FILE_PATH
	global acquire_print
	
	log = ''

	while(True):
		text = (conn.recv(1024)).decode('UTF-8')
		if(not text):
			break
		log = log + text

	with acquire_print:
		with open(FILE_PATH, 'a') as f:
			f.write(log)

	print('Got the info closing connection:', str(addr))
	conn.close()
	
if __name__ == '__main__':
        
        socket_object = socket.socket()
        socket_object.bind((get_ip(), PORT))
        socket_object.listen(5)

        while(True):
                conn, addr = socket_object.accept()
                print('Connection from:', addr)
                threading.Thread(target=log_info, args=(conn,addr)).start()
         
        socket_object.close()
