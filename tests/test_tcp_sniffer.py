import threading

from mamba_utils.mock.tcp_server_mock import TcpServerMock
from mamba_utils.tcp_sniffer import tcp_sniffer, tcp_client


class TestClass:
    def test_tcp_server_mock(self):
        host_ip, host_port = '127.0.0.1', 10001
        server_ip, server_port = '127.0.0.1', 10002

        mock = TcpServerMock(server_ip, server_port)

        sniffer = threading.Thread(target=tcp_sniffer,
                                   args=(host_ip, host_port, server_ip,
                                         server_port))
        sniffer.start()

        import time
        time.sleep(.1)

        reply = tcp_client(host_ip, host_port, b"Hello World 1")
        assert reply == b'HELLO WORLD 1'
        reply = tcp_client(host_ip, host_port, b"Hello World 2")
        assert reply == b'HELLO WORLD 2'
        reply = tcp_client(host_ip, host_port, b"Hello World 3")
        assert reply == b'HELLO WORLD 3'

        tcp_client(host_ip, host_port, b"shutdown")

        mock.shutdown()
        sniffer.join()
