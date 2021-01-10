from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Biodata,Portfolio,Skill,Services, Testimony,Certificate,Experience, ProductCategory

def update(request):
    #p=request.user.pk
    pass
    return render(request, 'index.html', {})

def profile(request,id):
    biodatas = Biodata.objects.get(user_id=id)
    portfolios = Portfolio.objects.filter(user_id=id)
    apps = Portfolio.objects.filter(user_id=id, category=1)
    cards = Portfolio.objects.filter(user_id=id, category=2)
    webs = Portfolio.objects.filter(user_id=id, category=3)
    skills = Skill.objects.filter(user_id=id)
    services = Services.objects.filter(user_id=id)
    testimonies = Testimony.objects.filter(recipient=id)
    certificates = Certificate.objects.filter(user_id=id)
    experience = Experience.objects.filter(user_id=id)
    categories = ProductCategory.objects.all()
    return render(request, 'index.html', {'apps':apps,'cards':cards,'webs':webs,'categories':categories,'certificates':certificates,'experience':experience,'biodatas':biodatas, 'portfolios':portfolios, 'skills':skills, 'services':services, 'testimonies':testimonies})

def portfolio_detail(request,id):
    portfolio=Portfolio.objects.get(id=id)
    return render(request, 'portfolio-details.html', {'portfolio':portfolio})

@login_required(login_url='loan:login')
def card(request):
    context={}
    return render(request, 'card.html', context)