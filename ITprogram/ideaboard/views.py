from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView,
    )
from django.http import Http404
from ideaboard.models import Post, User
from typing import Any, List
from django.shortcuts import render
from django.core.paginator import Paginator
from ideaboard.forms import PostForm, ProfileForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

class IndexView(LoginRequiredMixin,ListView):
    model = Post
    template_name = "ideaboard/index.html"
    context_object_name = "posts"
    paginate_by = 20
    ordering = ["-dt_created"]

def idea_detail(request,main_menu):
    context = dict()
    if main_menu in ["idea-archive","all-time-ranking","my-page"]:
        context["main_menu"] = "ここは"+main_menu+"です。"
        context["description"] = "まだ開発中です。"
    else:
        raise Http404("！！存在しないページです。")
    return render(request,'ideaboard_base/detail.html',context=context)

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = "ideaboard/view_detail.html"
    pk_url_kwarg = "post_id" 

#pk_url_kwarg: データを照会する条件キー#

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    template_name = "ideaboard/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.category = form.cleaned_data['category']
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("view_detail", kwargs={"post_id": self.object.id})

#self.object: 該当するGeneric Viewのオブジェクト#

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    form_class = PostForm
    template_name = "ideaboard/post_form.html"
    pk_url_kwarg = "post_id"

    #アクセス権限がない接近#
    raise_exception = True

    def get_success_url(self):
        return reverse("view_detail", kwargs={"post_id": self.object.id})
    
    def test_func(self):
        #修正するオブジェクトを持ってくる#
        post = self.get_object()
        return post.author == self.request.user
    
    def form_valid(self, form):
        # category update #
        self.object.category = form.cleaned_data['category']
        self.object.save()
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    template_name = "ideaboard/post_confirm_delete.html"
    pk_url_kwarg = "post_id"

    raise_exception = True


    def get_success_url(self):
        return reverse("index")
    
    def test_func(self):
        #修正するオブジェクトを持ってくる#
        post = self.get_object()
        return post.author == self.request.user

class ProfileView(DetailView):
    model = User
    template_name = "ideaboard/profile.html"
    pk_url_kwarg = "user_id" 
    context_object_name = "profile_user"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs.get("user_id")
        return context
    
class ProfileUpdateView(LoginRequiredMixin,UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "ideaboard/profile_update.html"

    def get_object(self, queryset=None):
        return self.request.user
    
    def get_success_url(self):
        return reverse("profile", kwargs={"user_id": self.request.user.id})