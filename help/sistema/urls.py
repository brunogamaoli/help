from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)), # Url para pagina de admin
    url(r'^base/', include('base.urls', namespace='base', app_name = 'base')), # Url para o app base
    url(r'^aluno/', include('aluno.urls', namespace='aluno', app_name = 'aluno')), # Url para o app aluno
    url(r'^', include('usuarios.urls', namespace='usuarios', app_name = 'usuarios'))
]
