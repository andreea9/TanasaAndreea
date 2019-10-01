



# Create your views here.

from django.shortcuts import render
from .models import User


def user_list(request):
    users = User.objects.all()

    context = {
        'users': users,

    }
    return render(request, 'list.html', context)