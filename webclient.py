import socket
from argparse import ArgumentParser

parser = ArgumentParser("HTTP client")
parser.add_argument("domain", type=str)
parser.add_argument("port", type=int, default=80, nargs="?")

args = parser.parse_args()
domain = args.domain
port = args.port

s = socket.socket()

request_data = f"GET / HTTP/1.1\r\nHost: {domain}\r\nConnection: close\r\n\r\n".encode(
    "ISO-8859-1"
)

s.connect((domain, port))
s.sendall(request_data)

while True:
    response = s.recv(4096)
    if len(response) == 0:
        break
    print(response.decode("ISO-8859-1"))

s.close()
