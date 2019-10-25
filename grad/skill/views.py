from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from skill.forms import AddSkill
from . models import SkillSet
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login

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

# def edit_skill(request):
#     return redirect('')