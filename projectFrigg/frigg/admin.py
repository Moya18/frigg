from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(Client)
admin.site.register(Design)
admin.site.register(PrinterType)
admin.site.register(Quote)
admin.site.register(Instructions)
admin.site.register(Job)
admin.site.register(Flag)