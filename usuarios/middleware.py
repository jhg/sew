from usuarios.models import Usuario

class Autenticacion(object):
    def process_request(self, request):
        if 'uid' in request.session:
            request.user = Usuario.objects.get(id=request.session['uid'])
        usuario = Usuario(id=0, nombre_usuario="anonimo", es_anonimo=True)
        usuario.save = lambda: None
        request.user = usuario
