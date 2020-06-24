import socket
import time
import socketserver
import argparse


def udp_client(ip: str, port: int, message: str) -> str:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.connect((ip, port))
        sock.sendall(message)
        return sock.recv(1024)


class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]

        reply = udp_client(self.server.server_ip, self.server.server_port,
                           data)

        print(f'[{time.time()}] Incoming: {data}')
        print(f'[{time.time()}] Outgoing: {reply}')

        socket.sendto(reply, self.client_address)

        if data == b'shutdown':
            exit()


def udp_sniffer(host_ip: str, host_port: int, server_ip: str,
                server_port: int) -> None:
    with socketserver.UDPServer((host_ip, host_port), MyUDPHandler) as server:
        server.server_ip = server_ip
        server.server_port = server_port
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print('Mamba UDP Sniffer Finalized')


def main():
    parser = argparse.ArgumentParser(description='UDP Sniffer.')
    parser.add_argument('host_port', type=int, help='Host port')
    parser.add_argument('server_port', type=int, help='Server port')
    parser.add_argument('--host_ip', type=str, help='Host ip')
    parser.add_argument('--server_ip', type=str, help='Server ip')

    args = parser.parse_args()

    udp_sniffer(args.host_ip or '127.0.0.1', args.host_port, args.server_ip
                or '127.0.0.1', args.server_port)


if __name__ == "__main__":
    main()
