import socket

from mamba_utils.mock.udp_server_mock import UdpServerMock
from mamba_utils.udp_client import udp_client


class TestClass:
    def test_udp_server_mock(self):
        host, port = '127.0.0.1', 9999

        mock = UdpServerMock(host, port)

        reply = udp_client(host, port, b"Hello World 1")
        assert reply == b'HELLO WORLD 1'
        reply = udp_client(host, port, b"Hello World 2")
        assert reply == b'HELLO WORLD 2'
        reply = udp_client(host, port, b"Hello World 3")
        assert reply == b'HELLO WORLD 3'

        mock.shutdown()
