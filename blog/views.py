from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import ContactForm
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib import messages
from .forms import LoginForm


# Create your views here.
def post_list(request):
   posts = Post.objects.all()
   return render(request, 'post_list.html',{'posts' : posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    return render(request,'post_detail.html',{'post' : post, 'comments' : comments})
 
def contact_view(request):
   if request.method == 'POST':
       form = ContactForm(request.POST)
       if form.is_valid():
          #Process the data here (e.g., send an email or save it to the database)
          name = form.cleaned_data['name']
          email = form.cleaned_data['email']
          message = form.cleaned_data['message']
          return render(request, 'blog/success.html',{'name':name})
       
   else:
       form = ContactForm()
       
   return render(request, 'blog/contact.html',{'form':form})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user but don't log them in
            messages.success(request, 'Signing up successful! Please log in.')  
            return redirect('login')  # Redirect to the login page
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('post_list')  # Redirect to the post list after login
    else:
        form = LoginForm()
    return render(request, 'blog/login.html', {'form': form})
