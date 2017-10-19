class MiddleWare(object):
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        import datetime
        print(datetime.datetime.now())
        return self.app(environ, start_response)
