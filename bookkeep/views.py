from django.shortcuts import render


# Create your views here.

def main_view(pRequest):
    return render(pRequest, 'bookkeep/qwe.html', {})
