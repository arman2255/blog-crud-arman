from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import SignUpForm, PostForm
from .models import Post


# ---------- HOME ----------
def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})


# ---------- SIGN UP ----------
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "🎉 Signup successful! Please log in.")
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})


# ---------- LOGIN ----------
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"👋 Welcome back, {user.username}!")
            next_url = request.GET.get('next')
            return redirect(next_url or 'home')
        else:
            messages.error(request, "⚠️ Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})


# ---------- LOGOUT ----------
def logout_view(request):
    logout(request)
    messages.success(request, "👋 You have been logged out successfully.")
    return redirect('home')


# ---------- CREATE POST ----------
@login_required(login_url='login')
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "✅ Blog created successfully!")
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})


# ---------- POST DETAIL ----------
@login_required(login_url='login')
def post_detail(request, post_id):
    """Private view — shows full blog details for logged-in users."""
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})


# ---------- LIKE / UNLIKE ----------
@login_required(login_url='login')
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post_detail', post_id=post.id)


# ---------- MY BLOGS ----------
@login_required
def my_blogs(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'blog/my_blogs.html', {'posts': posts})



# ---------- EDIT BLOG ----------
@login_required(login_url='login')
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Blog updated successfully!")
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/edit_post.html', {'form': form})



# ---------- DELETE BLOG ----------
@login_required(login_url='login')
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Permission check
    if not request.user.is_superuser and post.author != request.user:
        messages.error(request, "❌ You can only delete your own posts.")
        return redirect('home')

    if request.method == 'POST':
        post.delete()
        messages.success(request, "🗑️ Blog deleted successfully!")
        return redirect('my_blogs')

    return render(request, 'blog/post_confirm_delete.html', {'post': post})
