from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from forum.forms import PostForm
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login
from accounts.models import UserProfile
from django.core.mail import send_mail

# Create your views here.
def view_post(request):
    form = PostForm()
    posts = Post.objects.order_by('date').reverse()
    args = {'form':form,'posts':posts}
    return render(request,'forum/view.html',args)
    

    
@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            p = form.save(commit = False)
            p.user = request.user
            p.save()
            post = UserProfile.objects.all().filter(subscribe = True)
            ls = list()
            for a in post:
                posts = User.objects.all().filter(id = a.user_id)
                for e in posts:
                    ls.append(e.email)
            send_mail (
                'Confirmation mail',
                'Hey check out the new post.You dont gotta miss on this one :3',
                'peddi.vinil@gmail.com',
                ls,
        fail_silently = False,
    )
            return redirect('/forum/')
    else:
        form = PostForm()
        args = {'form':form}
        return render(request,'forum/create.html',args)

def full_post(request,id):
	post= get_object_or_404(Post, id=id)
	return render(request, 'forum/post.html', {'post':post})





