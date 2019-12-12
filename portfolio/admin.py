from django.contrib import admin
from .models import Portfolio

# Register your models here.
class PortfolioAdmin(admin.ModelAdmin):
    """ Show helpful fields on the changelist page. """
    list_display = ('title', 'slug', 'author', 'created')
#class ImageAdmin(admin.ModelAdmin):
    
admin.site.register(Portfolio, PortfolioAdmin)
    