import asyncio

from loguru import logger


class ProtocolFactory(asyncio.Protocol):
    def __init__(self, server):
        self.transport = None
        self.server = server

    def connection_made(self, transport):
        self.transport = transport
        logger.info('Connection from {}'.format(transport.get_extra_info('peername')))

    def data_received(self, data):
        logger.info('Data received: {!r}'.format(data))

    def connection_lost(self, exc):
        logger.info('The client closed the connection')
