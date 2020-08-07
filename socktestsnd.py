from socket import socket,AF_INET,SOCK_STREAM

HOST	= 'localhost'
PORT	= 51000

CHR_CAN	= '\18'
CHR_EOT	= '\04'

def com_send(mess):
	while True:
		try:
			sock = socket(AF_INET, SOCK_STREAM)
			sock.connect((HOST, PORT))
			sock.send(mess.encode('utf-8'))
			sock.close()
			break
		except:
			print('retry: ' + mess)

def proc():
	com_send('TTAPtest')

def exit():
	com_send(CHR_EOT)

def cancel():
	com_send(CHR_CAN)


proc()
proc()
proc()
cancel()
proc()
exit()

