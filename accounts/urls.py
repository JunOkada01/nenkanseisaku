# from django.urls import path
# from . import views
# urlpatterns = [
#     path("signup/", views.signup, name="signup"),
#     path("signin/", views.signin, name="signin"),
# ]
# urlpatterns = [
#     path('', views.index, name='index'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('signinsent', views.signinsent, name='signinsent'),
    path('signupsent', views.signupsent, name='signupsent'),
]