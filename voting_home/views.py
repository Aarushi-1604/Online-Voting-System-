from django.shortcuts import render
from django.contrib import messages
# Create your views here.
def voting_homepage(request):
    if request.session.get('show_welcome_message'):
        messages.success(request,'Welcome Back!')
        del request.session['show_welcome_message']
    return render(request,'voting_homepage.html')