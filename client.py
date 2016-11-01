import requests, tornado, argparse, webbrowser, socket
from tornado import httpclient

CRLF = "\r\n\r\n"

def clargs():
	parser = argparse.ArgumentParser(description='Send a GET request to echo.php on port 8000 of the localhost.')
	parser.add_argument('-m', '--message', required=False, help='Message to echo')
	parser.add_argument('-p', '--port', type=int, required=False, help='Port to connect to')
	parser.add_argument('-o', '--host', required=False, help='Host name to send get request to')
	return parser.parse_args()

def sendGet(message='Test', port=80, host='localhost'):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# now connect to the web server on port 80 - the normal http port
	s.connect((host, port))
	request = "GET /echo.php?message={1} HTTP/1.0{0}".format(CRLF, message)
	s.send(request.encode('utf-8'))
	data = (s.recv(1000000))
	s.shutdown(1)
	s.close()
	print('Received', data.decode("utf-8"))

if __name__ == '__main__':
	args = clargs()
	if args.message is not None:
		m = args.message
	else:
		m = 'Test'
	if args.port is not None:
		p = args.port
	else:
		p = 8000
	if args.host is not None:
		h = args.host
	else:
		h = 'localhost'
	sendGet(message=m, port=p, host=h)









