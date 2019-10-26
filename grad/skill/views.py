from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from skill.forms import AddSkill
from . models import SkillSet
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login
from collections import Counter
import matplotlib.pyplot as plt
import os

@login_required
def add_skill(request):
    if request.method == "POST":
        form = AddSkill(request.POST)
        if form.is_valid():
            p = form.save(commit = False)
            p.user = request.user
            p.save()
            return redirect('/about/')
        else:
            return redirect('/forum/')
    else:
        form = AddSkill()
        args = {'form':form}
        return render(request,'skill/add_skill.html',args)

def anal_skill(request):
    post = SkillSet.objects.all()
    lang = list()
    frame = list()
    gpas = list()
    newlan = list()
    newfra = list()
    for e in post:
        a=str(e.languages)
        b=str(e.frameworks)
        lang.append(a.split(","))
        frame.append(b.split(","))
        gpas.append(e.gpa)
    for i in lang:
        newlan = newlan+i
    for j in frame:
        newfra = newfra+j
    dix = dict(Counter(newlan))
    diy = dict(Counter(newfra))
    hit(gpas)
    pit(dix)
    #pit(diy)  
    return render(request,'skill/analysis.html')


def pit(dix):

    labels = dix.keys()
    sizes = slices=dix.values()
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Programming Language Analysis')
    fig1 = plt.gcf()
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    imag=os.path.join(BASE_DIR,'accounts/static/')
    print(imag)
    fig1.savefig(imag+'pie/pie1.jpg', dpi=100)

def hit(dix):
    
  
    # setting the ranges and no. of intervals 
    range = (5, 10) 
    bins = 20  
    
    # plotting a histogram 
    plt.hist(dix, bins, range, color = 'green', 
            histtype = 'bar', rwidth = 0.5) 
    
    # x-axis label 
    plt.xlabel('GPA') 
    # frequency label 
    plt.ylabel('Frequency') 
    # plot title 
    plt.title('GPA Plot') 
    fig1 = plt.gcf()
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    imag=os.path.join(BASE_DIR,'accounts/static/')
    print(imag)
    fig1.savefig(imag+'hit.jpg', dpi=100)