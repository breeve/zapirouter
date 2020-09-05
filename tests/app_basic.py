from ApiRouter import ApiRouter
from ApiRouter import Route
from ApiRouter import route_updates
from ApiRouter import Logger
from ApiRouter import LoggerConfig



log = Logger()

app_route = Route()

@app_route.route('/', methods=['GET'])
def index():
    log.info('hello z... api router')

if ('__name__' == '__main__') :
    # app
    app = ApiRouter(log_config=LoggerConfig(level='DEBUG'))

    # init route
    app.route_update(app_route)

    # run
    app.route_dump()
    app.run(demaon=False)
