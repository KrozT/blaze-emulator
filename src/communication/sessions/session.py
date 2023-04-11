class Session:
    def __init__(self, transport):
        self.transport = transport

    def send(self, data):
        self.transport.write(data)
