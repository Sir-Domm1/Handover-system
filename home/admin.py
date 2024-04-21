from django.contrib import admin
from .models import Handover, Notices,Comment

# Register your models here.
class HandoverAdmin(admin.ModelAdmin):
    pass
admin.site.register(Handover,HandoverAdmin)


class NoticesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Notices,NoticesAdmin)

class CommentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Comment,CommentAdmin)


