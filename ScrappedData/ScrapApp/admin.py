from django.contrib import admin



# Register your models here.
from .models import BrowseItems
@admin.register(BrowseItems)
class StudentAdmin(admin.ModelAdmin):
    list_display=('name','price','description','image_link')



