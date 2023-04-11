import asyncio
import threading

from network.handler import Handler


class Server(threading.Thread):
    def __init__(self, host, port):
        threading.Thread.__init__(self)  # Call the Thread class's init function

        self.loop = asyncio.get_event_loop()  # Create an event loop
        self.coro = self.loop.create_server(lambda: Handler(self), host, port)  # Create a server
        self.server = self.loop.run_until_complete(self.coro)  # Start the server

    def run(self):
        self.loop.run_forever()  # Run the event loop forever

    def close(self):
        self.server.close()  # Close the server
        self.loop.run_until_complete(self.server.wait_closed())  # Wait for the server to close
        self.loop.close()  # Close the event loop
