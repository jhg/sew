from usuarios import models

class Autenticacion(object):
    def process_request(self, request):
        # NOTA: Falta que busque el objeto de usuario adecuado o cree uno
        #        anonimo
        if 'usuario_id' in request.session:
            request.user = request.session['usuario_id']
        request.user = None
