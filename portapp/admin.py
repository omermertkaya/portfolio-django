from django.contrib import admin
from .models import HomeSection,MyServicesSection,AboutMeSection,StorySection, WorkSection, WebLogoName, FooterSection

# Register your models here.
admin.site.register(WebLogoName)
admin.site.register(HomeSection)
admin.site.register(MyServicesSection)
admin.site.register(AboutMeSection)
admin.site.register(StorySection)
admin.site.register(WorkSection)
admin.site.register(FooterSection)
