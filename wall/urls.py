from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('p/<slug:slug>/', views.PostView.as_view(), name='post_view'),
    path('r/<category>', views.CategoryView.as_view(), name='category_view'),
    path('delete/<category>', views.delete_category, name='delete_category'),
    path('delete_post/<slug:slug>', views.delete_post, name='delete_post'),
    path('new_post', views.NewPostView.as_view(), name='new_post'),
    path('new_category', views.NewCategoryView.as_view(), name='new_category'),
    path('edit_profile', views.EditProfile.as_view(), name='edit_profile'),
    path(
        'coming_soon/<str:feature>',
        views.ComingSoon.as_view(),
        name='coming_soon'
        ),
    path('like/<slug:slug>', views.LikePost.as_view(), name='post_like')
]
