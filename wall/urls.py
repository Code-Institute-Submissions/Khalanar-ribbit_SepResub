from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('p/<slug:slug>/', views.PostView.as_view(), name='post_view'),
    path('r/<category>', views.CategoryView.as_view(), name='category_view'),
    path('new_post', views.NewPostView.as_view(), name='new_post')

]