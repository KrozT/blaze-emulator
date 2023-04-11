import asyncio


class Handler(asyncio.Protocol):
    def __init__(self, server):
        self.transport = None
        self.server = server

    def connection_made(self, transport):
        self.transport = transport
        print('Connection from {}'.format(transport.get_extra_info('peername')))

    def data_received(self, data):
        print('Data received: {!r}'.format(data))

    def connection_lost(self, exc):
        print('The client closed the connection')
