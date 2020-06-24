import socket
import time
import argparse


def tcp_client(ip: str, port: int, message: str) -> str:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        sock.sendall(message)
        reply = sock.recv(1024)
        sock.close()
        return reply


def main():
    parser = argparse.ArgumentParser(description='TCP Server Mock.')
    parser.add_argument('server_port', type=int, help='Server port')
    parser.add_argument('msg', type=str, help='Message')
    parser.add_argument('--server_ip', type=str, help='Server ip')

    args = parser.parse_args()

    msg = bytes(args.msg, 'ascii')

    print(f'[{time.time()}] Outgoing: {msg}')

    reply = tcp_client(args.server_ip or '127.0.0.1', args.server_port,
                       msg)

    print(f'[{time.time()}] Incoming: {reply}')


if __name__ == "__main__":
    main()
