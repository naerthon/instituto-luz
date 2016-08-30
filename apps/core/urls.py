from django.conf.urls import url
from .views import turma,alunos,add_alunos,edit_alunos,detail_turma,add_aula, add_situacao,situacao


urlpatterns = [
    url(r'^$', turma, name='index'),
    url(r'^alunos/$', alunos, name='alunos'),
    url(r'^alunos/add$', add_alunos, name='add-alunos'),
    url(r'^alunos/editar/(?P<pk>[0-9]+)/$', edit_alunos, name='editar-aluno'),
    url(r'^turma/(?P<pk>[0-9]+)/$', detail_turma, name='detail-turma'),
    url(r'^aula/add/(?P<pk>[0-9]+)/$', add_aula, name='add-aulas'),
    url(r'^status/add/(?P<pk>[0-9]+)/$', add_situacao, name='add-situacao'),
    url(r'^status/(?P<pk>[0-9]+)/$', situacao, name='situacao'),
]