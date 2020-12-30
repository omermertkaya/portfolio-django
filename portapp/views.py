from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView,CreateView
from .models import PostHome2,PostHome3,PostHome4,Story_Bolumu, Work_Bolumu
from django.template import Context, loader
from django.utils import timezone
 



def HomeView(request):

    obj = PostHome2.objects.get(id=1)
    context5= {
    'cv_isim_soyisim' : obj.cv_isim_soyisim,
    'cv_Meslek' : obj.cv_Meslek,
    'cv_fotograf_1': obj.cv_fotograf_1
    }

    obj2 = PostHome3.objects.get(id=1)
    context2= {
        'baslik_1' : obj2.baslik_1,
        'aciklama_1' : obj2.aciklama_1,
        'baslik_2' : obj2.baslik_2,
        'aciklama_2' : obj2.aciklama_2,
        'baslik_3' : obj2.baslik_3,
        'aciklama_3' : obj2.aciklama_3,

    }

    obj3 = PostHome4.objects.get(id=1)
    context3={
        'who_baslik' : obj3.who_baslik,
        'who_aciklama' : obj3.who_aciklama,
        'who_fotograf' : obj3.who_fotograf,
    }

    obj4 = Story_Bolumu.objects.get(id=1)
    context4={
        'story_baslik' : obj4.story_baslik,
        'story_aciklama' : obj4.story_aciklama,
        'story_fotograf' : obj4.story_fotograf,

    }
        
    context2.update(context5)
    context2.update(context3)
    context2.update(context4)

    # post_list = Work_Bolumu.objects.all() 
   
    #return render(request, 'work.html', context)

    post_liste = Work_Bolumu.objects.all() 

   

    


    return render(request, "index.html",{"context2":context2,"post_liste":post_liste})


class ArticleDetailBolumu(DetailView):
    model = Work_Bolumu
    template_name='article_details.html'
        
      
    
    

    
    
    

   






    





   




    


