from django.contrib import admin
from .models 		import Aluno, Curso, Aula, Turma, Frequencia, Situacao
from django.db 		import models
# Register your models here.

class AlunoAdmin(admin.ModelAdmin):
    fields = ('nome', 'cidade', 'estado','bairro', 'data_nascimento', 'fone', 'whatsapp','data_criacao','data_atualizacao',)

class AulaAdmin(admin.ModelAdmin):
    fields = ('aula','turma', 'data')
    list_filter = ('turma',)
    date_hierarchy = 'data'

class TurmaAdmin(admin.ModelAdmin):
    fields = ('turma', 'curso','aluno', 'instrutor', 'limite_faltas', 'data_inicio', 'data_termino','ativo')

class FrequenciaAdmin(admin.ModelAdmin):
    list_display = ('aula', 'aluno', 'frequencia')

admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Aula, AulaAdmin)
admin.site.register(Frequencia, FrequenciaAdmin)
admin.site.register(Situacao)
admin.site.register(Curso)
