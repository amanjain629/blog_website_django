from django.urls.base import reverse_lazy
from django.views.generic.edit import DeleteView
from blogapp.forms import PostForm
from django import forms
from blogapp.models import Catagory, Post
from django.shortcuts import render,get_object_or_404
from django.views.generic import DetailView,ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy, reverse
from blogapp.forms import PostForm,EditForm
from django.http import HttpResponseRedirect
# Create your views here.
# def index(request):
#     return render(request,'index.html')

class HomeView(ListView):
    model=Post
    template_name='index.html'
    ordering=['-date_post']

    def get_context_data(self,*args, **kwargs):
        cat_menu=Catagory.objects.all()
        context=super(HomeView,self).get_context_data(*args, **kwargs)
        context["cat_menu"]=cat_menu
        return context

class ArticleView(DetailView):
    model=Post
    template_name='article.html'

    def get_context_data(self,*args, **kwargs):
        cat_menu=Catagory.objects.all()

        stuff=get_object_or_404(Post, id=self.kwargs['pk'])
        liked=False
        if stuff.like.filter(id=self.request.user.id).exists():
            liked=True

        total_likes=stuff.total_likes()
        context=super(ArticleView,self).get_context_data(*args, **kwargs)
        context["cat_menu"]=cat_menu
        context["total_likes"]=total_likes
        context['liked']=liked
        return context

class AddPostView(CreateView):
    model=Post
    form_class=PostForm
    template_name='add_post.html'
    # fields='__all__'
    # fields=('title','title_tag','body')

def LikeView(request,pk):
    post=get_object_or_404(Post,id=request.POST.get('post_id'))
    liked=False
    if post.like.filter(id=request.user.id).exists():
        post.like.remove(request.user)
        liked=False
    else:
        post.like.add(request.user)
        liked=True

    return HttpResponseRedirect(reverse('article-detail',args=[str(pk)]))


def CategoryListView(request):
    cat_menu_list=Catagory.objects.all()
    return render(request,'category-list.html',{'cat_menu_list':cat_menu_list})

def CatagoryView(request,cats):
    catagory_posts=Post.objects.filter(catagory=cats.replace('-',' '))
    return render(request,'catagories.html',{'cats':cats.title().replace('-',' '),'catagory_posts':catagory_posts})

class AddCatagoryView(CreateView):
    model=Catagory
    template_name='add_catagory.html'
    fields='__all__'

class EditPostView(UpdateView):
    model=Post
    template_name='edit_post.html'
    form_class=EditForm
    # fields=['title','title_tag','body']

class DeletePostView(DeleteView):
    model=Post
    template_name='delete_post.html'
    success_url=reverse_lazy("index")