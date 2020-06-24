import socket

from mamba_utils.mock.udp_server_mock import UdpServerMock


def client(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.connect((ip, port))
        sock.sendall(bytes(message, 'ascii'))
        return str(sock.recv(1024), 'ascii')


class TestClass:
    def test_udp_server_mock(self):
        host, port = '127.0.0.1', 9999

        mock = UdpServerMock(host, port)

        reply = client(host, port, "Hello World 1")
        assert reply == 'HELLO WORLD 1'
        reply = client(host, port, "Hello World 2")
        assert reply == 'HELLO WORLD 2'
        reply = client(host, port, "Hello World 3")
        assert reply == 'HELLO WORLD 3'

        mock.shutdown()
