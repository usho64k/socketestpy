from socket import socket, AF_INET, SOCK_STREAM

HOST		= 'localhost'
PORT		= 51000
L_MAX_MSG	= 2048
NUM_THREAD	= 4

CHR_CAN		='\18'
CHR_EOT		='\04'

def com_receive():
	sock = socket(AF_INET, SOCK_STREAM)
	sock.bind((HOST,PORT))
	sock.listen(NUM_THREAD)
	print('receiver ready, NUM_thReAD = ' + str(NUM_THREAD))

	while True:
		try:
			conn,addr = sock.accept()
			mess = conn.recv(L_MAX_MSG).decode('utf-8')
			conn.close()
			if(mess == CHR_EOT):
				break
			if(mess == CHR_CAN):
				print('cancel')
				continue
			print('message' + mess)
		except Exception as e:
			print('Error args:' , e.args)
	
	sock.close()
	print('end of receiver')

def proc():
	com_receive()


proc()
