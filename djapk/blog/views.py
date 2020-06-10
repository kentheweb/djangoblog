from django.shortcuts import render, redirect
from .models import Post
from .forms import addPost
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def home(request):
    post = Post.objects.order_by('date_created')
    context = {
        'posts':post
    }
    return render(request, 'blog/home.html', context)

@login_required
def createpost(request):
    if request.method == 'POST':
        form = addPost(request.POST)
        title = Post(title=request.POST['title'], post=request.POST['post'])
        title.save()
        return redirect('home-route')
    else:    
        form = addPost()
    context = {
        'forms' : form
    }
    return render(request, 'blog/create.html', context)


class createPost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'post']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ViewPosts(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_created']
    paginate_by = 2
    
class EachPost(LoginRequiredMixin, DetailView):
    model = Post

class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'post']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = post.get_object()
        if post.author == self.request.user:
            return True
        else:
            return False

def about(request):
    return render(request, 'blog/about.html')

