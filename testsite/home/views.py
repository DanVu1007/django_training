from django.shortcuts import render
# Create your views here.
def index(request):
    context = {
        'year': 2023,
    }
    return render(request, 'pages/home.html', context)
