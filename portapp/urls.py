from django.urls import path
from .views import HomeView,ArticleDetailBolumu
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',HomeView,name="index"),
    #path('article/<int:id>', ArticleDetailView.as_view(), name='article-detail'),
    #path("article/<int:pk>", ArticleDetailBolumu.as_view(), name="article-detail"),

    
    
   
   
    
] 





