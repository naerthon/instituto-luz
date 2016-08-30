from django.db import models
from django.contrib import admin
from .models import Aluno, Curso, Aula, Turma, Frequencia, Situacao
# Register your models here.

class AlunoAdmin(admin.ModelAdmin):
        fields = ('nome', 'cidade', 'estado','bairro', 'data_nascimento', 'fone', 'whatsapp','data_criacao','data_atualizacao',)

class AulaAdmin(admin.ModelAdmin):
        fields = ('aula','turma', 'data')

class TurmaAdmin(admin.ModelAdmin):
        fields = ('turma', 'curso','aluno', 'instrutor', 'limite_faltas', 'data_inicio', 'data_termino','ativo')

admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Aula, AulaAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Situacao)
admin.site.register(Curso)
@admin.register(Frequencia)
class FrequenciaAdmin(admin.ModelAdmin):
    list_display = ('aula', 'aluno', 'frequencia')