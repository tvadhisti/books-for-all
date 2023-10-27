from django.urls import path
from loginpage.views import register
from loginpage.views import login_user
from loginpage.views import logout_user
from . import views 

app_name = 'loginpage'

urlpatterns = [
path('register/', register, name='register'),
path('login/', login_user, name='login'),
path('logout/', logout_user, name='logout'),

]