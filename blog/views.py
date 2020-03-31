from django.shortcuts import render

def posts_list(request):
    names = ['Ivan', 'Kostya', 'Anya', 'Masha']
    return render(request, "blog/index.html", context={'names': names})
