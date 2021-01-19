from django.urls import path
from .views import HomeView,ArticleDetailBolumu,HomeSectionUpdateView,MyServicesSectionUpdateView,AboutMeSectionUpdateView
from .views import StorySectionUpdateView,WorkSectionUpdateView,FooterSectionUpdateView,WebLogoNameUpdateView
from .views import WorkSectionCreateView,WorkSectionDeleteView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',HomeView,name="index"),
    path("article/<int:pk>", ArticleDetailBolumu.as_view(), name="article-detail"),
    path("update/homesection/<int:pk>", HomeSectionUpdateView.as_view(), name="update-homesection"),
    path("update/myservicessection/<int:pk>", MyServicesSectionUpdateView.as_view(), name="update-myservicessection"),
    path("update/aboutmesection/<int:pk>", AboutMeSectionUpdateView.as_view(), name="update-aboutmesection"),
    path("update/storysection/<int:pk>", StorySectionUpdateView.as_view(), name="update-storysection"),
    path("update/worksection/<int:pk>", WorkSectionUpdateView.as_view(), name="update-worksection"),
    path("update/footersection/<int:pk>", FooterSectionUpdateView.as_view(), name="update-footersection"),
    path("update/weblogoname/<int:pk>", WebLogoNameUpdateView.as_view(), name="update-weblogoname"),
    path("add/worksection/", WorkSectionCreateView.as_view(), name="add-workseciton"),
    path("del/worksection/<int:pk>",WorkSectionDeleteView.as_view(), name ="del-worksection")

    
    
   
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







