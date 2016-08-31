from django                         import forms
from django.forms.extras.widgets    import SelectDateWidget
from apps.core.models               import Aluno, Aula,Turma, Situacao, Curso, Frequencia

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'data_nascimento', 'fone','whatsapp', 'cidade', 'estado', 'bairro',]
        widgets = {
        'nome': forms.TextInput(attrs={
            'placeholder':'Nome completo',
            'class':'form-control',
            'required':'required',
            
        }),
        'data_nascimento': forms.DateInput(
            attrs={
                'placeholder':'Data de Nascimento',
                'class':'date-picker form-control col-md-7 col-xs-12',
                'id':'birthday',
                'data-inputmask':"'mask': '99/99/9999'",
            },
            format=('%d-%m-%Y'),
            ),
        'fone': forms.TextInput(attrs={
            'placeholder':'Telefone',
            'class':'form-control',
            #'data-inputmask':"'mask' : '(999) 999-9999'",
            }),
        'whatsapp': forms.TextInput(attrs={
            'placeholder':'whatsapp',
            'class':'form-control',
            # 'data-inputmask':"'mask' : '(999) 999-9999'",
        }),
        'cidade': forms.TextInput(attrs={
            'placeholder':'Cidade',
            'class':'form-control',
            }),
        'estado': forms.TextInput(attrs={
            'placeholder':'Estado',
            'class':'form-control',
            }),
        'bairro': forms.TextInput(attrs={
            'placeholder':'Bairro',
            'class':'form-control',
            }),
        }


class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['turma', 'curso', 'aluno', 'instrutor', 'limite_faltas', 'data_inicio', 'data_termino', ]

# class SituacaoForm(forms.ModelForm):
#     class Meta:
#         model = Situacao
#         fields = [
#             'curso',
#             'aluno',
#         ]
#         widgets = {
#             'curso' : forms.Select(attrs={
#                 'placeholder':'Nome completo',
#                 'class':'form-control',
#             }),
#             'aluno' : forms.Select(attrs={
#                 'placeholder':'Nome completo',
#                 'class':'form-control',
#             }),
#         }

class FrequenciaForm(forms.ModelForm):

    class Meta:
        model = Frequencia
        fields = ['frequencia','id']
        labels = {
            "frequencia": False,
        }
        
        
        
class AulaForm(forms.ModelForm):

    class Meta:
        model = Aula
        fields = ['aula','turma','data']
        widgets = {
            'aula' : forms.TextInput(attrs={
                'placeholder':'Aula',
                'class':'form-control',
            }),
            'turma' : forms.TextInput(attrs={
                'placeholder':'Turma',
                'class':'form-control',
                'readonly':"readonly",
            }),
            'data': forms.DateInput(
                attrs={
                    'placeholder':'Data de Nascimento',
                    'class':'date-picker form-control col-md-7 col-xs-12',
                    'id':'birthday',
                    'data-inputmask':"'mask': '99/99/9999'",
                },
                format=('%d-%m-%Y'),
            ),
        }

class SearchForm(forms.Form):
    inicio = forms.DateTimeField(
        widget=forms.DateInput(format='%y-%m-%d',
            attrs={
            'class':'datepicker form-control col-md-4',
            'id':'inicio',
            }))
    fim = forms.DateTimeField(
        widget=forms.DateInput(format='%y-%m-%d',
            attrs={
            'class':'datepicker form-control col-md-4',
            'id':'fim',
            }))

