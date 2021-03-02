from django.contrib import admin
from models import Post
#admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_data')
admin.site.register(Post,PostAdmin)
# Register your models here.
