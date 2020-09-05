from .app import Application
from .log import Logger, LoggerConfig
from .route import Route, route_updates

class ApiRouter():
    # logger
    logger = None

    # application
    server = '127.0.0.1'
    port = 2222
    app = None

    # router
    route = None

    def __init__(self, server=None, port=None):
        if (server != None) :
            self.server = server
        if (port != None) :
            self.port = port
        
        self.logger = Logger()

        self.app = Application(self.server, self.port)

        self.route = Route()

        return self.app

    @classmethod
    def logger_get():
        return self.logger

    @classmethod
    def route_update(route):
        self.route = route_update(self.route, route)

    @classmethod
    def route_dump():
        self.route.dump()

    @classmethod
    def run(demaon=True):
        logger.debug('{} : {} start'.format(self.server, str(self.port)))
