from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Contact)
admin.site.register(Information)
admin.site.register(Services)
admin.site.register(Portfoliocategory)
admin.site.register(Portfolio)
admin.site.register(Blog)
admin.site.register(BlogCategory)
admin.site.register(BlogComment)
