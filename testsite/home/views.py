from django.shortcuts import render
from megamenu.models import MegaMenu
# Create your views here.
def index(request):
    megaMenu = MegaMenu.objects.get(use_on_fe=1)

    context = {
        'year': 2023,
        'megamenu': megaMenu

    }
    return render(request, 'pages/home.html', context)
