from django.db                  import models
from django.utils               import timezone
from django.contrib.auth.models import User
from django.db.models.signals   import pre_save, post_save
from django.dispatch            import receiver
import datetime
from datetime import date


class Aluno(models.Model):

    nome = models.CharField(max_length=255, verbose_name='Nome Completo')
    data_nascimento = models.DateField(verbose_name='Data de nascimento')
    fone = models.CharField(max_length=13, verbose_name='Telefone',)
    whatsapp = models.CharField(max_length=13, verbose_name='Whatsapp',)
    cidade = models.CharField(max_length=255, verbose_name='Cidade')
    estado = models.CharField(max_length=255, verbose_name='Estado')
    bairro = models.CharField(max_length=255, verbose_name='Bairro')
    data_criacao = models.DateTimeField(verbose_name='Data de criação', default=timezone.now)
    data_atualizacao = models.DateTimeField(verbose_name='Data de atualização', default=timezone.now)

    class Meta:
        ordering = ["nome"]
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    def __str__(self):
        return self.nome


class Curso(models.Model):
    CURSO=(
        ('Conheça o espiritísmo','Conheça o espiritísmo'),
        ('Nosso Lar','Nosso Lar'),
        ('Passe','Passe'),
        ('Corrente Magnética','Corrente Magnética'),
    )

    curso = models.CharField(max_length=255, verbose_name='Curso', choices=CURSO, default=1)
    class Meta:
        ordering = ["id"]
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):

        return self.curso
CURSO=(
    ('1','Conheça o espiritísmo'),
    ('2','Nosso Lar'),
    ('3','Passe'),
    ('4','Corrente Magnética'),
)

PERIODO=(
    (1,"{}.{}".format(date.today().year, '1')),
    (2,"{}.{}".format(date.today().year, '2')),
    (3,"{}.{}".format(date.today().year, '3')),
)

class Turma(models.Model):
    turma = models.IntegerField(verbose_name='Período da Turma', choices=PERIODO, default=1)
    curso = models.CharField(max_length=1,verbose_name='Curso', choices=CURSO, default='1')
    aluno = models.ManyToManyField(Aluno, blank=True)
    instrutor = models.ForeignKey(User, default=1)
    limite_faltas = models.IntegerField(verbose_name='Limite de faltas', default=2)
    data_inicio = models.DateField(verbose_name='Data de início')
    data_termino = models.DateField(verbose_name='Data de término')
    data_criacao = models.DateTimeField(verbose_name='Data de criação', default=timezone.now)
    data_atualizacao = models.DateTimeField(verbose_name='Data de atualização', default=timezone.now)
    ativo = models.BooleanField(default=True)

    class Meta:
        unique_together = ('curso', 'turma')
        ordering = ["turma"]
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'

    def __str__(self):
        return '%s - %s' % (self.get_curso_display(), self.get_turma_display())

@receiver(pre_save, sender=Turma)
def verifica_ativo(sender, instance, **kwargs):
    if instance.data_termino >= datetime.date.today():
        instance.ativo=True
    else:
        instance.ativo=False

class FrequenciaManager(models.Manager):
    def create_freq(self, aula,aluno):
        send = self.create(aula_id=aula, aluno_id=aluno)
        return send

class Aula(models.Model):
    aula = models.CharField(max_length=255, verbose_name='Descriminação da aula')
    turma = models.ForeignKey(Turma)
    data = models.DateField(verbose_name='Data da aula')
    data_criacao = models.DateTimeField(verbose_name='Data de criação', default=timezone.now)
    data_atualizacao = models.DateTimeField(verbose_name='Data de atualização', default=timezone.now)

    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'

    def __str__(self):
        return '%s - %s' % (self.data, self.turma)


class Frequencia(models.Model):

    aula = models.ForeignKey(Aula)
    aluno = models.ForeignKey(Aluno, null=True, blank=True, verbose_name='Aluno')
    frequencia = models.BooleanField(default=1)
    data_criacao = models.DateTimeField(verbose_name='Data de criação', default=timezone.now)
    data_atualizacao = models.DateTimeField(verbose_name='Data de atualização', default=timezone.now)
    objects = FrequenciaManager()

    class Meta:
        unique_together = ('aula', 'aluno')
        ordering = ["aula"]
        verbose_name = "Frequência"
        verbose_name_plural = 'Frequências'

    def __str__(self):
        return '%s - %s' % (self.aluno, self.aula)


class SituacaoManager(models.Manager):
    def create_situacao(self, pk,aluno):
        send = self.create(turma_id=pk, aluno_id=aluno)
        return send


class Situacao(models.Model):
    CHOICES_SITUACAO = (
        ('1', 'Apto',),
        ('2', 'Inapto por frequência'),
    )

    turma      = models.ForeignKey(Turma)
    aluno      = models.ForeignKey(Aluno)
    frequencia = models.IntegerField(null=True, blank=True, default=0)
    situacao   = models.CharField(max_length=255, verbose_name='Situação', choices=CHOICES_SITUACAO, default='1')
    objects    =SituacaoManager()

    class Meta:
        ordering = ["aluno","turma"]
        verbose_name = "Situação"
        verbose_name_plural = 'Situação'

    def __str__(self):
        return '%s - %s' % (self.aluno, self.turma)


def apto_ou_inapto(sender, instance, **kwargs):
    cont = Frequencia.objects.filter(aluno=instance.aluno, aula__turma__id=instance.turma_id, frequencia=False).count()
    if cont <= instance.turma.limite_faltas:
        instance.situacao = '1'
    else:
        instance.situacao = '2'
    instance.frequencia = cont
pre_save.connect(apto_ou_inapto, sender=Situacao)