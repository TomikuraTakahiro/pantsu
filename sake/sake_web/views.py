from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from sake_web.models import sake,otumami
from sake_web.forms import SearchSakeForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from .forms import (
    LoginForm
)

User = get_user_model()
# Create your views here.
def top(request):
    """トップページ"""
    Sakes = sake.objects.all().order_by('id')
    return render(request,
                  'sake_web/top.html',
                    {'sakes': Sakes})

def sake_list(request):
    """酒の検索"""

    form = SearchSakeForm()

    if request.method == 'GET':

        Sakes = sake.objects.all().order_by('id')
        return render(request,
                      'sake_web/sake_search.html',
                     {'form':form,'sakes': Sakes}
                     ,RequestContext(request))
    elif request.method == 'POST':

        form = SearchSakeForm(request.POST)

        if form.is_valid():
            Search = form.save(commit=False)
            Sakes = sake.objects.all().order_by('id')
            Sakes = Sakes.filter(name = Search.name)
            return render(request,
                      'sake_web/sake_search.html',
                     {'form':form,'sakes': Sakes}
                     ,RequestContext(request))

def mypage(request):
    """マイページ"""
    return render(request,
                  'sake_web/mypage.html')

def otumami_list(request):

    Otumamis = otumami.objects.all().order_by('id')
    return render(request,
              'sake_web/otumami.html',
             {'otumamis': Otumamis}
             ,RequestContext(request))

class sake_detail(generic.DetailView):
    model = sake
    """酒の詳細"""
    template_name = 'sake_web/sake_detail.html'

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'sake_web/signup.html'

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'registration/login.html'

class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'sake_web/top.html'

class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser


class UserDetail(OnlyYouMixin, generic.DetailView):
    model = User
    template_name = 'sake_web/user_detail.html'
