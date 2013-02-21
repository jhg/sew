from usuarios.models import Usuario

class Autenticacion(object):
    def process_request(self, request):
        if 'uid' in request.session:
            request.user = Usuario.objects.get(id=request.session['uid'])
            request.user.anonimo = False
            request.user.is_authenticated = lambda: True
            request.user.esta_autenticado = lambda: True
        usuario = Usuario(id=0, nombre_usuario="anonimo")
        usuario.save = lambda: None
        usuario.is_authenticated = lambda: False
        usuario.esta_autenticado = lambda: False
        usuario.anonimo = True
        request.user = usuario
