from django.urls import path
from sake_web import views
from django.urls import include
from . import views

app_name = 'sake_web'
urlpatterns = [
    # 書籍
    path('top/', views.top, name='top'),                  #トップ
    path('search/', views.sake_list, name='sake_list'),   #酒一覧
    path('search/detail',views.sake_detail,name='sake_detail'), #酒詳細
    path('mypage/', views.mypage, name='my_page'),        #マイページ
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('user_detail/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('user_update/<int:pk>/', views.UserUpdate.as_view(), name='user_update'),
    ]
