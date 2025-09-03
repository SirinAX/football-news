from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406495792',
        'name': 'Andi Hakim Himawan',
        'class': 'PBP-D'
    }

    return render(request, "main.html", context)