from django.contrib import admin
from .models 		import Aluno, Curso, Aula, Turma, Frequencia, Situacao
from django.db 		import models
# Register your models here.

class AlunoAdmin(admin.ModelAdmin):
    fields = ('nome', 'cidade', 'estado','bairro', 'data_nascimento', 'fone', 'whatsapp','data_criacao','data_atualizacao',)
    list_display = ('nome', 'cidade', 'fone', 'whatsapp')
    list_filter = ('data_nascimento','nome',)
    search_fields = ('nome',)
    list_per_page = 10

class AulaAdmin(admin.ModelAdmin):
    fields = ('aula','turma', 'data')
    list_filter = ('turma',)
    date_hierarchy = 'data'
    list_per_page = 10

class TurmaAdmin(admin.ModelAdmin):
    fields = (('curso','turma'),'aluno', 'instrutor', 'limite_faltas', ('data_inicio', 'data_termino'),'ativo')
    list_display = ('curso', 'turma', 'instrutor', 'ativo')
    filter_horizontal=['aluno']
    list_display_links = ('curso', 'turma',)
    list_filter = ('curso','ativo')
    search_fields = ('turma','aluno__nome',)
    date_hierarchy = 'data_inicio'
    list_per_page = 10

class FrequenciaAdmin(admin.ModelAdmin):
    list_display = ('aula', 'aluno', 'frequencia')
    list_filter = ('aula__turma','frequencia','aluno',)
    search_fields = ('aluno__nome',)
    list_per_page = 10

    # def get_turma(self, obj):
    #     return obj.aula.aula

admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Aula, AulaAdmin)
admin.site.register(Frequencia, FrequenciaAdmin)
admin.site.register(Situacao)
#admin.site.register(Curso)
