import socket
import time
import socketserver
import argparse


def tcp_client(ip: str, port: int, message: bytes) -> bytes:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        sock.sendall(message)
        reply = sock.recv(1024)
        sock.close()
        return reply


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def handle(self):
        # self.request is the TCP socket connected to the client
        data = self.request.recv(1024).strip()

        if data == b'shutdown':
            raise KeyboardInterrupt()

        reply = tcp_client(self.server.server_ip, self.server.server_port,
                           data)

        print(f'[{time.time()}] Incoming: {data}')
        print(f'[{time.time()}] Outgoing: {reply}')

        self.request.sendall(reply)


def tcp_sniffer(host_ip: str, host_port: int, server_ip: str,
                server_port: int) -> None:
    socketserver.TCPServer.allow_reuse_address = True
    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((host_ip, host_port), MyTCPHandler) as server:
        server.server_ip = server_ip
        server.server_port = server_port

        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print('Mamba TCP Sniffer Finalized')


def main():
    parser = argparse.ArgumentParser(description='TCP Sniffer.')
    parser.add_argument('host_port', type=int, help='Host port')
    parser.add_argument('server_port', type=int, help='Server port')
    parser.add_argument('--host_ip', type=str, help='Host ip')
    parser.add_argument('--server_ip', type=str, help='Server ip')

    args = parser.parse_args()

    tcp_sniffer(args.host_ip or '127.0.0.1', args.host_port, args.server_ip
                or '127.0.0.1', args.server_port)


if __name__ == "__main__":
    main()
