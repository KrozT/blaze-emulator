import asyncio

from loguru import logger


class ProtocolFactory(asyncio.Protocol):
    def __init__(self, server, message_handler):
        self.transport = None
        self.server = server
        self.message_handler = message_handler

    def connection_made(self, transport):
        self.transport = transport
        logger.info('Connection from {}'.format(transport.get_extra_info('peername')))

    def data_received(self, data):
        self.message_handler.handle(self.transport, data, None)  # Very primitive, needs to be improved

    def connection_lost(self, exc):
        logger.info('The client closed the connection')
