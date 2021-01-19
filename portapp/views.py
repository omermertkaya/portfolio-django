from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView
from .models import HomeSection,MyServicesSection,AboutMeSection,StorySection, WorkSection, WebLogoName, FooterSection
from django.template import Context, loader
from django.utils import timezone
from django.views.generic.edit import UpdateView 
from django.urls import reverse_lazy

 



def HomeView(request):

    obj = HomeSection.objects.get(id=1)
    context5= {
    'cv_name_surname' : obj.cv_name_surname,
    'cv_job' : obj.cv_job,
    'cv_photo': obj.cv_photo
    }

    obj2 = MyServicesSection.objects.get(id=1)
    context2= {
        'title_1' : obj2.title_1,
        'content_1' : obj2.content_1,
        'title_2' : obj2.title_2,
        'content_2' : obj2.content_2,
        'title_3' : obj2.title_3,
        'content_3' : obj2.content_3,

    }

    obj3 = AboutMeSection.objects.get(id=1)
    context3={
        'who_title' : obj3.who_title,
        'who_content' : obj3.who_content,
        'who_photo' : obj3.who_photo,
    }

    obj4 = StorySection.objects.get(id=1)
    context4={
        'story_title' : obj4.story_title,
        'story_content' : obj4.story_content,
        'story_photo' : obj4.story_photo,

    }

    obj5 = WebLogoName.objects.get(id=1)
    context6={
        'web_name' : obj5.web_name,
        'web_logo' : obj5.web_logo,
    }

    obj6 = FooterSection.objects.get(id=1)
    context7 ={
        'footer_linked' : obj6.footer_linked,
        'footer_github' : obj6.footer_github,
        'footer_instagram' : obj6.footer_instagram,
        'footer_facebook' : obj6.footer_facebook,
        'footer_email' : obj6.footer_email,
    }
        
    
    context2.update(context3)
    context2.update(context4)
    context2.update(context5)
    context2.update(context6)
    context2.update(context7)

    # post_list = Work_Bolumu.objects.all() 
   
    #return render(request, 'work.html', context)

    print(context7)

    post_liste = WorkSection.objects.all() 

   

    


    return render(request, "index.html",{"context2":context2,"post_liste":post_liste})


class ArticleDetailBolumu(DetailView):
    model = WorkSection
    template_name='article_details.html'

    def get_context_data(self, **kwargs):
        context1 = super().get_context_data(**kwargs)
        context1["WebLogoName"] = WebLogoName.objects.get(id=1)
        context2 = super().get_context_data(**kwargs)
        context2["FooterSection"] = FooterSection.objects.get(id=1)
        context2.update(context1)
        return context2


class HomeSectionUpdateView(UpdateView):
    model = HomeSection
    template_name = "update_homesection.html"
    fields = ['cv_name_surname','cv_job','cv_photo']
    success_url ="/"
    
    def get_context_data(self, **kwargs):
        context1 = super().get_context_data(**kwargs)
        context1["WebLogoName"] = WebLogoName.objects.get(id=1)
        context2 = super().get_context_data(**kwargs)
        context2["FooterSection"] = FooterSection.objects.get(id=1)
        context3 = super().get_context_data(**kwargs)
        context3["HomeSection"] = HomeSection.objects.get(id=1)

        context1.update(context2)
        context1.update(context3)
    
        
        return context1

class MyServicesSectionUpdateView(UpdateView):
    model = MyServicesSection
    template_name = "update_myservicessection.html"
    fields = ['title_1','content_1','title_2','content_2','title_3','content_3']
    success_url ="/"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["FooterSection"] = FooterSection.objects.get(id=1)
        context1 = super().get_context_data(**kwargs)
        context1["WebLogoName"] = WebLogoName.objects.get(id=1)
        context.update(context1)
        return context

class AboutMeSectionUpdateView(UpdateView):
    model = AboutMeSection
    template_name = "update_aboutmesection.html"
    fields = ['who_title','who_content','who_photo']
    success_url ="/"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["FooterSection"] = FooterSection.objects.get(id=1)
        context1 = super().get_context_data(**kwargs)
        context1["WebLogoName"] = WebLogoName.objects.get(id=1)
        context2 = super().get_context_data(**kwargs)
        context2["AboutMeSection"] = AboutMeSection.objects.get(id=1)
        context.update(context2)
        context.update(context1)
        return context


class StorySectionUpdateView(UpdateView):
    model = StorySection
    template_name="update_storysection.html"
    fields=['story_title','story_content','story_photo']
    success_url ="/"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["FooterSection"] = FooterSection.objects.get(id=1)
        context1 = super().get_context_data(**kwargs)
        context1["WebLogoName"] = WebLogoName.objects.get(id=1)
        context2 = super().get_context_data(**kwargs)
        context2["StorySection"] = StorySection.objects.get(id=1)
        context.update(context2)
        context.update(context1)
        return context
     
class WorkSectionUpdateView(UpdateView):
    model = WorkSection
    template_name = "update_worksection.html"
    fields=['work_name','work_sub_title_black','work_sub_title','work_article_photo','work_index_photo','work_content']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["FooterSection"] = FooterSection.objects.get(id=1)
        context1 = super().get_context_data(**kwargs)
        context1["WebLogoName"] = WebLogoName.objects.get(id=1)
        context2 = super().get_context_data(**kwargs)
        context2["WorkSection"] = WorkSection.objects.all()
        context.update(context2)
        context.update(context1)
        return context

class FooterSectionUpdateView(UpdateView):
    model = FooterSection
    template_name = "update_footersection.html"
    fields=['footer_linked','footer_github','footer_instagram','footer_facebook','footer_email']
    success_url ="/"
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["FooterSection"] = FooterSection.objects.get(id=1)
            context1 = super().get_context_data(**kwargs)
            context1["WebLogoName"] = WebLogoName.objects.get(id=1)
            context.update(context1)
            return context

class WebLogoNameUpdateView(UpdateView):
    model = WebLogoName
    template_name = "update_weblogoname.html"
    fields=['web_name','web_logo']
    success_url ="/"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["FooterSection"] = FooterSection.objects.get(id=1)
        context1 = super().get_context_data(**kwargs)
        context1["WebLogoName"] = WebLogoName.objects.get(id=1)
        context.update(context1)
        return context


class WorkSectionCreateView(CreateView):
    model = WorkSection
    template_name = "add_worksection.html"
    fields=['work_name','work_sub_title_black','work_sub_title','work_article_photo','work_index_photo','work_content']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["FooterSection"] = FooterSection.objects.get(id=1)
        context1 = super().get_context_data(**kwargs)
        context1["WebLogoName"] = WebLogoName.objects.get(id=1)
        context2 = super().get_context_data(**kwargs)
        context2["WorkSection"] = WorkSection.objects.all()
        context.update(context2)
        context.update(context1)
        return context

class WorkSectionDeleteView(DeleteView):
    model = WorkSection
    template_name = "del_worksection.html"
    success_url = reverse_lazy('index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["FooterSection"] = FooterSection.objects.get(id=1)
        context1 = super().get_context_data(**kwargs)
        context1["WebLogoName"] = WebLogoName.objects.get(id=1)
        context2 = super().get_context_data(**kwargs)
        context2["WorkSection"] = WorkSection.objects.all()
        context.update(context2)
        context.update(context1)
        return context







    
    
    
    


    



















# def ArticleDetailBolumu(requset):

#     post_liste2 = Work_Bolumu.objects.all() 

#     obj = WebLogoName.objects.get(id=1)
#     context6={
#         'web_name' : obj.web_name,
#         'web_logo' : obj.web_logo,
#     }
        

#     return render(request, "article_details.html",{"context2":context2,"post_liste":post_liste})


    





        
      
    
    

    
    
    

   






    





   




    


