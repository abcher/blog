from django.db import models
from django.contrib import admin
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
#blogs ordering minus mean desc
    class Meta:
        pass
        # ordering = ('-timestamp',) #desc


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')




admin.site.register(BlogPost,BlogPostAdmin)