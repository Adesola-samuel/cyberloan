from django.contrib import admin
from .models import Contributor, Help, Prediction

class ContributorAdmin(admin.ModelAdmin):
    list_display = ('name', 'office',)


class HelpAdmin(admin.ModelAdmin):
    list_display = ('task',)


class PredictionAdmin(admin.ModelAdmin):
    list_display = ('name', 'loan_amount', 'loan_status',)


admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Help, HelpAdmin)
admin.site.register(Prediction, PredictionAdmin)