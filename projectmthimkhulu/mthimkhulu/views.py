from django.shortcuts import render


def index(request):

    context = {

    }

    return render(request, 'mthimkhulu/index.html', context)