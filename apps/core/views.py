from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models     import Group, User
from django.shortcuts               import render, redirect, get_object_or_404, render_to_response
from django.forms                   import modelformset_factory
from django.http                    import HttpResponse, HttpResponseRedirect
from .models                        import Aluno, Aula, Situacao, Curso, Turma, Frequencia
from .forms                         import AlunoForm, FrequenciaForm, AulaForm, SearchForm

@login_required
def index(request):
    template_name = 'index.html'
    return render(request, template_name, {})


@login_required
@permission_required('Admin')
def alunos(request):
    bread=request.path.split('/')[:-1]
    template_name = 'alunos/alunos.html'
    rows = Aluno.objects.all()
    context = {
        'rows' : rows,
        'bread' : bread
    }
    return render(request, template_name, context)


@login_required
@permission_required('Admin')
def add_alunos(request):
    template_name = 'alunos/add.html'
    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            form = form.save()
            form.save()
            return redirect('/alunos/')
    else:
        form = AlunoForm()
    return render(request, template_name, {'form': form})


@login_required
@permission_required('Admin')
def edit_alunos(request, pk):
    template_name = 'alunos/editar.html'
    form = get_object_or_404(Aluno, pk=pk)
    if request.method == "POST":
        form = AlunoForm(request.POST, instance=form)
        if form.is_valid():
            form = form.save()
            form.save()
            return redirect('/alunos/', pk=form.pk)

    else:
        form = AlunoForm(instance=form)
    return render(request, template_name, {'form': form})


@login_required
def turma(request):
    template_name = 'turma/index.html'
    rows = Turma.objects.filter(instrutor=request.user,ativo=True)
    turmas = Turma.objects.all()
    for turma in turmas:
        turma=Turma.objects.get(pk=turma.id)
        turma.ativo=None
        turma.save()

    return render(request, template_name, locals())


@login_required
def detail_turma(request, pk, *args, **kwarg):
    bread=request.path.split('/')[1]
    template_name = 'turma/detail.html'
    rows = get_object_or_404(Turma, pk=pk)
    if not rows.instrutor==request.user:
        #request.flash['notice'] = 'something wrong'
        return HttpResponseRedirect("/")
    alunos = Turma.aluno.through.objects.filter(turma_id=pk).order_by('aluno','id')
    aulas = Aula.objects.filter(turma_id=pk).order_by('data')
    query=Frequencia.objects.filter(aula__turma__id=pk).order_by('aluno','aula__data','aula__id')

    FrequenciaFormSet = modelformset_factory(Frequencia,
        form=FrequenciaForm,
        fields=("id","frequencia"),
        extra=0
        )

    form=None
    if request.method=='POST' and 'search-inicio' in request.POST:
        search=SearchForm(request.POST,prefix='search')
        if search.is_valid():
            form_was_submitted = True
            cd = search.cleaned_data
            aulas = Aula.objects.filter(turma_id=pk, data__range=[cd['inicio'],cd['fim']]).order_by('data')
            query = Frequencia.objects.filter(aula__turma__id=pk, aula__data__range=[cd['inicio'],cd['fim']]).order_by('aluno','aula__data','aula__id')

    if request.method=='POST' and not 'search-inicio' in request.POST:
        formset=FrequenciaFormSet(request.POST, prefix='frequencia')
        if formset.is_valid():
            for f in formset:
                f.save()
            return redirect('/turma/%i' % int(pk))
    else:
        try:
            formset=FrequenciaFormSet(queryset=query, prefix='frequencia')
            if len(alunos)>0:
                f=formset.total_form_count()/len(alunos)
            else:
                return HttpResponse('Formset não gerado', status=400)

            forms=[]
            a=0
            b=int(f)
            for x in alunos:
                forms.append(formset[a:b])
                a+=int(f)
                b+=int(f)
            form=zip(alunos,forms)
        except:
            return HttpResponse('fim', status=400)

        search=SearchForm(prefix='search')


    context = dict(
        aulas=aulas,
        rows=rows,
        forms=form,
        formset=formset,
        query=query,
        search=search,
        alunos=alunos,
        bread=bread,
        )

    return render(request, template_name, context)


@login_required
def add_aula(request,pk):
    template_name='aula/add.html'
    alunos = Turma.aluno.through.objects.filter(turma_id=pk).order_by('aluno').values('aluno')
    form = AulaForm(request.POST)
    if form.is_valid():
        form=form.save()
        print(form.id)
        for aluno in alunos:
            Frequencia.objects.create_freq(form.id,aluno['aluno'])
        return redirect('/turma/%i' % int(pk))
    else:
        form = AulaForm(initial={'turma': pk})
    return render(request, template_name, locals())


@login_required
def add_situacao(request,pk):
    turma  = Turma.objects.get(pk=pk)
    alunos = Turma.aluno.through.objects.filter(turma_id=pk).order_by('aluno')
    for aluno in alunos:
        Situacao.objects.update_or_create(turma=turma,aluno=aluno.aluno)
    return redirect('/status/%i' % int(pk))


@login_required
def situacao(request,pk):
    template_name = 'situacao/situacao.html'
    rows = Situacao.objects.filter(turma_id=pk)
    context = {'rows' : rows}
    print(rows)
    return render(request, template_name, context)