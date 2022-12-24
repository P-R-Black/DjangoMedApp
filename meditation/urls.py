from django.urls import path
from . import views


app_name = 'meditation'
urlpatterns = [
    path('', views.index_page, name='index'),
    path('history/', views.history_page, name='history'),
    path('ajax_test/', views.ajax_test, name='ajax_test'),
    path('meditate/', views.meditate_page, name='meditate'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

]
