from django.conf import settings
from django.utils.importlib import import_module
import requests


def get_adapter(adapter):
    # grab the classname off of the backend string
    package, klass = adapter.rsplit('.', 1)

    # dynamically import the module, in this case app.backends.adapter_a
    module = import_module(package)

    # pull the class off the module and return
    return getattr(module, klass)


class BaseAdapter:

    def get(self, uri):
        raise NotImplemented


class RequestsAdapter(BaseAdapter):

    def get(self, uri):
        r = requests.get(uri)
        return r.text


class Fetcher:

    def __init__(self):
        adapter = getattr(settings,
                          'FETCHER_BACKEND',
                          'event.fetch.RequestsAdapter')
        self.backend = get_adapter(adapter)()

    def get(self, uri):
        return self.backend.get(uri)

