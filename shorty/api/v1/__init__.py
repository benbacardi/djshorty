from .resources import ShortURLResource
from tastypie.api import Api

api = Api(api_name='v1')
api.register(ShortURLResource())
