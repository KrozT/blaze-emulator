import asyncio
import threading

from loguru import logger

from network.protocol_factory import ProtocolFactory


class Server(threading.Thread):
    def __init__(self, host, port):
        threading.Thread.__init__(self)  # Call the Thread class's init function

        self.loop = asyncio.get_event_loop()  # Create an event loop
        self.coro = self.loop.create_server(lambda: ProtocolFactory(self), host, port)  # Create a server
        self.server = self.loop.run_until_complete(self.coro)  # Start the server

    def run(self):
        logger.info('Server running on [{}] - port: [{}]'.format(self.server.sockets[0].getsockname()[0],
                                                                 self.server.sockets[0].getsockname()[1]))
        self.loop.run_forever()  # Run the event loop forever

    def close(self):
        self.server.close()  # Close the server
        self.loop.run_until_complete(self.server.wait_closed())  # Wait for the server to close
        self.loop.close()  # Close the event loop

        logger.info('Server closed successfully')  # Log that the server has been closed
