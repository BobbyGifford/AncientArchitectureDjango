from django.shortcuts import render, get_object_or_404
from .models import Theory
from accounts.models import Profile


def index(request):
    theories = Theory.objects.order_by('-upload_date')

    context = {
        'theories': theories
    }
    return render(request, 'theories/theories.html', context)


def theory(request, theory_id):
    theory_by_id = get_object_or_404(Theory, pk=theory_id)

    evidence_list = theory_by_id.evidence.split(', ')

    context = {
        'theory': theory_by_id,
        'evidence': evidence_list
    }
    return render(request, 'theories/theory.html', context)


def add_theory(request):
    context = {
        'add_or_update': 'Add',
        theory: 'new_theory'
    }
    if request.method == 'POST':
        new_theory = Theory(
            profile=Profile.objects.get(user=request.user),
            title=request.POST['title'],
            theory=request.POST['theory'],
            evidence=request.POST['evidence'],
            youtube_link=request.POST['youtube_link']
        )

        if 'main_image' in request.FILES:
            new_theory.main_image = request.FILES['main_image']
        new_theory.save()
        return render(request, 'theories/theory.html', context)

    return render(request, 'theories/add_theory.html', context)


def edit_theory(request, theory_id):
    old_theory = Theory.objects.get(pk=theory_id)

    context = {
        'add_or_update': 'Update',
        'theory': old_theory
    }
    if request.method == 'POST':
        old_theory.title = request.POST['title']
        old_theory.theory = request.POST['theory']
        old_theory.evidence = request.POST['evidence']
        old_theory.youtube_link = request.POST['youtube_link']

        if 'main_image' in request.FILES:
            old_theory.main_image = request.FILES['main_image']

        old_theory.save()
        return render(request, 'theories/theory.html', context)

    return render(request, 'theories/add_theory.html', context)


def delete_theory(request, theory_id):
    Theory.objects.filter(id=theory_id).delete()
    return index(request)
