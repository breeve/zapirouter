import os

class LoggerConfig():
    def __init__(self, level='INFO'):
        print('test')

class Logger():
    def __init__(self, config=None):
        print('test')

    @classmethod
    def debug(self, msg):
        print('DEBUG | {}'.format(str(msg)))

    @classmethod
    def info(self, msg):
        print('INFO | {}'.format(str(msg)))