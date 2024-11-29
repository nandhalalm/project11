from django.contrib import admin
from .models import Details,Marks


class newdetails(admin.ModelAdmin):
    list_display=('name','age','user','phone','address')
    search_fields=('phone','name')
    list_filter=('age','address')
    ordering=('-id',)

admin.site.register(Details,newdetails)

class newmarks(admin.ModelAdmin):
    list_display=('english','science','maths')
    search_fields=('english',)
    list_filter=('english',)


admin.site.register(Marks,newmarks)