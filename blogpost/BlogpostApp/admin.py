from django.contrib import admin
from .models import BlogPost,Comment,CustomUser,Block
from rangefilter.filters import DateRangeFilter,DateTimeRangeFilter
# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title","author","created_date","updated_date")
    list_filter = (('created_date',DateTimeRangeFilter),)
    search_fields = ("title","content")



    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.author):
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and (request.user == obj.author):
            return True
        return False

    def save_model(self, request, obj, form, change):
        obj.author=request.user
        super().save_model(request,obj,form,change)

admin.site.register(BlogPost,BlogPostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['com_content',]
    def has_change_permission(self, request, obj=None):
        if obj is not None and (request.user==obj.com_author):
            return True
        return False
admin.site.register(Comment,CommentAdmin)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("name",)
admin.site.register(CustomUser,CustomUserAdmin)

class BlockAdmin(admin.ModelAdmin):
    pass
admin.site.register(Block,BlockAdmin)

