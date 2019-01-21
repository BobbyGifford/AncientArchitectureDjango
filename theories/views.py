from django.shortcuts import render, get_object_or_404
from .models import Theory
from accounts.models import Profile


def index(request):
    theories = Theory.objects.all()

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
    return render(request, 'theories/add_theory.html')
