from mamba_utils.mock.tcp_server_mock import TcpServerMock
from mamba_utils.tcp_client import tcp_client


class TestClass:
    def test_tcp_server_mock(self):
        host, port = '127.0.0.1', 9998

        mock = TcpServerMock(host, port)

        reply = tcp_client(host, port, b"Hello World 1")
        assert reply == b'HELLO WORLD 1'
        reply = tcp_client(host, port, b"Hello World 2")
        assert reply == b'HELLO WORLD 2'
        reply = tcp_client(host, port, b"Hello World 3")
        assert reply == b'HELLO WORLD 3'

        mock.shutdown()
