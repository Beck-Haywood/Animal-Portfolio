from django.contrib import admin

# Register your models here.
from .models import Portfolio


class PortfolioAdmin(admin.ModelAdmin):
    """ Show helpful fields on the changelist page. """
    list_display = ('title', 'slug', 'author', 'created', 'picture')


admin.site.register(Portfolio, PortfolioAdmin)
