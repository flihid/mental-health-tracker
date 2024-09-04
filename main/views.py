from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306245831',
        'name': 'Mohamad Rafli Hidayat',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)