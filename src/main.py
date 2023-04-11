import os

from dotenv import load_dotenv
from network.server import Server


def initialize():
    load_dotenv()  # Load the .env file

    server = Server(os.getenv('SERVER_IP'), os.getenv('SERVER_PORT'))  # Create a server
    server.start()  # Start the server


if __name__ == '__main__':
    initialize()
