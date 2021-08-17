from django.urls import path
from . import views

urlpatterns = [
    path('', views.MoviesView.as_view(), name='home'),
    path('filter/', views.FilterMoviesView.as_view(), name='filter'),
    path('search/', views.Search.as_view(), name='search'),
    path("add-rating/", views.AddStarRating.as_view(), name='add_rating'),
    path('category/', views.CategoryView.as_view(), name='category_view'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('<slug:slug>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('<str:name>/', views.CategoryDetailView.as_view(), name='cat_detail'),
    path('review/<int:pk>/', views.AddReview.as_view(), name='add_review'),
    path('actor/<str:slug>/', views.ActorView.as_view(), name='actor_detail'),
]
