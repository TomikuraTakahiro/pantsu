from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from .models import sake,otumami,otumami_detail,otumami_with_sake,tag,tag_relation,advas,like,event,event_manage

class sakeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','creater')
    list_display_links = ('id', 'name',)

admin.site.register(sake, sakeAdmin)

class otumamiAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')

admin.site.register(otumami, otumamiAdmin)
