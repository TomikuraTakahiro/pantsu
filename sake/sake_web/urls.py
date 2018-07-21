from django.urls import path
from sake_web import views
from django.urls import include
from . import views

app_name = 'sake_web'
urlpatterns = [
    # 書籍
    path('top/', views.top, name='top'),                  #トップ
    path('search/', views.sake_list, name='sake_list'),   #酒一覧
    path('otumami/', views.otumami_list, name='otumami_list'),
    path('search/detail/<int:pk>/',views.sake_detail.as_view(),name='sake_detail'), #酒詳細
    path('mypage/', views.mypage, name='my_page'),        #マイページ
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('user_detail/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    ]
