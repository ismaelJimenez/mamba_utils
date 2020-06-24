import threading
import time

from mamba_utils.mock.udp_server_mock import UdpServerMock
from mamba_utils.udp_sniffer import udp_sniffer, udp_client


class TestClass:
    def test_udp_server_mock(self):
        host_ip, host_port = '127.0.0.1', 9999
        server_ip, server_port = '127.0.0.1', 10000

        mock = UdpServerMock(server_ip, server_port)

        sniffer = threading.Thread(target=udp_sniffer,
                                   args=(host_ip, host_port, server_ip,
                                         server_port))
        sniffer.start()

        time.sleep(.1)

        reply = udp_client(host_ip, host_port, b"Hello World 1")
        assert reply == b'HELLO WORLD 1'
        reply = udp_client(host_ip, host_port, b"Hello World 2")
        assert reply == b'HELLO WORLD 2'
        reply = udp_client(host_ip, host_port, b"Hello World 3")
        assert reply == b'HELLO WORLD 3'

        udp_client(host_ip, host_port, b"shutdown")

        mock.shutdown()
