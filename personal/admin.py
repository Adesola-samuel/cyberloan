from django.contrib import admin
from .models import Biodata,ProductCategory,Cities,Portfolio,Testimony,Services,Interest,Skill,Certificate,Experience

class BiodataAdmin(admin.ModelAdmin):
    list_display = ('user',)

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('user', 'awarded_qualification')

class InterestAdmin(admin.ModelAdmin):
    list_display = ('interest',)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill',)

class TestimonyAdmin(admin.ModelAdmin):
    list_display = ('author','recipient')

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('service',)

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Testimony, TestimonyAdmin)
admin.site.register(Biodata, BiodataAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Cities)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Services,ServicesAdmin)