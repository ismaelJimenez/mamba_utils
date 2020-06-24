import socket
import argparse


def udp_client(ip: str, port: int, message: str) -> str:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.connect((ip, port))
        sock.sendall(message)
        return sock.recv(1024)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='UDP Server Mock.')
    parser.add_argument('server_port', type=int, help='Server port')
    parser.add_argument('msg', type=str, help='Message')
    parser.add_argument('--server_ip', type=str, help='Server ip')

    args = parser.parse_args()

    print("Sent:     {}".format(args.msg))

    reply = udp_client(args.server_ip or '127.0.0.1', args.server_port, bytes(args.msg, 'ascii'))

    print("Received: {}".format(str(reply, 'ascii')))
