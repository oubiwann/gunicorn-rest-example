import functools

from bottle import Bottle as BottleBase
from bottle import get, post, put, delete

class Bottle(BottleBase):
    def patch(self, path=None, method='PATCH', **options):
        return self.route(path, method, **options)
    def options(self, path=None, method='OPTIONS', **options):
        return self.route(path, method, **options)
