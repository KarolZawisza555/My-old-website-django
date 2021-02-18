from django.urls import path
from . import views

app_name = 'resume'

urlpatterns = [
    path('', views.home, name='home'),
    path('about_me/', views.about_me, name='about_me'),
    path('education/', views.education, name='education'),
    path('expirience/', views.expirience, name='expirience'),
    path('website/', views.website, name='website'),
    path('contact/', views.contact, name='contact'),
    path('skills/', views.skills, name = 'skills'),
    path('back-end/', views.back, name = 'back'),
    path('skills/<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name = 'blog_detail'),
    path('skills/tag/<slug:tag_slug>/', views.skills, name='post_list_by_tag'),
    path('api/', views.api_list, name='api_list'),

    

            ]
