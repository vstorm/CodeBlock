from django.contrib import admin
from models import Press,Tag,Category
from my_comment_app.models import CommentWithReply

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cname',)
    search_field = ('cname',)
    
class TagAdmin(admin.ModelAdmin):
    list_display = ('tname',)
    search_field = ('taname',)
    
class PressAdmin(admin.ModelAdmin):
    list_display = ('title','date_pub','introduce',)
    search_field = ('title',)
    list_filter = ('tags','category')
    ordering = ('-date_pub',)
    
class CommentWithReplyAdmin(admin.ModelAdmin):
    list_display=('object_pk','content_object','user_name','submit_date')
    list_filter = ('object_pk',)
    ordering = ('-submit_date',)
    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Press,PressAdmin)
admin.site.register(CommentWithReply,CommentWithReplyAdmin)