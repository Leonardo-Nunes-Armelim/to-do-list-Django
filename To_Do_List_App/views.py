from django.shortcuts import render


def home(request):
    return render(request, 'To_Do_List_App/home.html')