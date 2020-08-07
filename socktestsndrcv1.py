from socket import socket,AF_INET,SOCK_STREAM

HOST		= 'localhost'
SPORT		= 51000
RPORT		= 50100
L_MAX_MSG	= 2048
NUM_THREAD	= 4

CHR_CAN	= '\18'
CHR_EOT	= '\04'

def com_send(mess):
	while True:
		try:
			sock = socket(AF_INET, SOCK_STREAM)
			sock.connect((HOST, SPORT))
			sock.send(mess.encode('utf-8'))
			sock.close()
			break
		except:
			print('retry: ' + mess)

def com_receive():
	sock = socket(AF_INET, SOCK_STREAM)
	sock.bind((HOST,RPORT))
	sock.listen(NUM_THREAD)
	print('receiver ready, NUM_THREAD = ' + str(NUM_THREAD))
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
		except Exception as e:
			print('Error args:' , e.args)
	
	sock.close()
	print('end of receiver')

def proc():
	com_send('TTAPtest')

def exit():
	com_send(CHR_EOT)

def cancel():
	com_send(CHR_CAN)


com_receive()
proc()
com_receive()
proc()
com_receive()
cancel()
com_receive()
proc()
com_receive()
exit()


