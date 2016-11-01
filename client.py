import requests, tornado, argparse, webbrowser, socket
from tornado import httpclient

CRLF = "\r\n\r\n"

def clargs():
	main_parser = argparse.ArgumentParser(description='Send a GET request to echo.php on port 8000 of the localhost.')
	main_parser.add_argument('-m', '--message', required=False, help='Message to echo')
	return main_parser.parse_args()

def sendGet2(message='Test'):
	client = httpclient.HTTPClient()
	request = tornado.httpclient.HTTPRequest(method='GET', url='http://localhost:8000/echo.php?message='+message)
	try:
		p = client.fetch(request)
		print(p.body)
	except httpclient.HTTPError as e:
		print("Error: "+ str(e))
	client.close()

def sendGet(message='Test'):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# now connect to the web server on port 80 - the normal http port
	s.connect(("localhost", 8000))
	request = "GET /echo.php?message={1} HTTP/1.0{0}".format(CRLF, message)
	s.send(request.encode('utf-8'))
	data = (s.recv(1000000))
	s.shutdown(1)
	s.close()
	print('Received', data.decode("utf-8"))

if __name__ == '__main__':
	args = clargs()
	if(args.message is not None):
		sendGet(args.message)
	else:
		sendGet()









