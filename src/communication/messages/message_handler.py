from communication.messages.events.login.VersionCheckMessageEvent import VersionCheckMessageEvent
from loguru import logger

import communication.headers.events as events


class MessageHandler:
    def __init__(self):
        self.messages = {
            events.VersionCheckMessageEvent: VersionCheckMessageEvent(),
        }

        logger.info('Message handler initialized with [{}] messages'.format(len(self.messages)))

    def handle(self, session, message_header, message):
        if message is not None:
            if message.header in self.messages:
                logger.info('Handling message: [{}]'.format(message.header))
                self.messages[message.header].handle(session, message)
            else:
                logger.warning('Unhandled message: [{}]'.format(message.header))
        else:
            logger.warning('Message is None, message header: [{}]'.format(message_header))
