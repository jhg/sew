from usuarios import models

class Autenticacion(object):
    def process_request(self, request):
        request.user = None
