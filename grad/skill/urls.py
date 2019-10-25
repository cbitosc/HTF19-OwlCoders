from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
 
urlpatterns = [
    path('add-skill/',views.add_skill,name='add_skill'),
    # path('edit-skill/',views.edit_skill,name='edit_skill'),
    # path('post/<int:id>/edit')
]