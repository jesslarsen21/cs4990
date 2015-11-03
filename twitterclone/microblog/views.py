from django.forms.models import model_to_dict
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.views.generic.detail import View, SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy, reverse
from django import forms
from .models import Tweet, Profile
from django.http import HttpResponseRedirect
from .forms import PostForm
# Create your views here.

class TweetListView(ListView):
    template_name = "tweet_list.html"
    model = Tweet
    paginate_by = 10

class ProfileView(DetailView):
    template_name = "profile.html"
    model = Profile

class MyFeedView(ListView):
    template_name = "myfeed.html"
    model = Tweet
    paginate_by = 10

    def get_queryset(self):
        my_profile = Profile.objects.get_or_create(user=self.request.user)
        my_profile = self.request.user.profile_set.all()[0]
        profile_list = list(my_profile.following.all())
        profile_list.append(my_profile)
        return Tweet.objects.filter(profile__in = profile_list)

class FollowForm(SingleObjectMixin, View):
    model = Profile

    def post(self, request, *args, **kwargs):
        my_profile = request.user.profile_set.all()[0]
        try:
            my_profile.following.add(self.kwargs['pk'])
            my_profile.save()
        except:
            return HttpResponseRedirect(reverse('microblog:followsuccess', args= (self.kwargs['pk'], )))
        #return HttpResponseRedirect(reverse('microblog:followsuccess', kwargs = {'pk': self.get_object().pk}))
        #if request.is_ajax():
        #    return Http
        return HttpResponseRedirect(reverse('microblog:followsuccess', args = (self.kwargs['pk'], )))


class FollowSuccessView(DetailView):
    template_name = 'follow_success.html'
    model = Profile

class CreatePost(FormView):
    template_name = 'post_form.html'
    form_class = PostForm

    def form_valid(self, form):
        post = Tweet()
        post.body = form.cleaned_data['body']
        post.profile = Profile.objects.get(pk=self.kwargs['pk'])
        post.save()
        return super(CreatePost, self).form_valid(form)


    def get_success_url(self):
        return reverse('microblog:userposts', args = (self.kwargs['pk'],))

class UpdateProfile(UpdateView):
    template_name = 'profile_form.html'
    model = Profile
    fields = ['profile_picture', 'bio']

    def get_success_url(self):
        return reverse('microblog:profileview', args=(self.kwargs['pk'],))

class UserPosts(ListView):
    template_name = "tweet_list.html"
    model = Tweet

    def get_queryset(self):
        return Tweet.objects.filter(profile = self.kwargs['pk'])