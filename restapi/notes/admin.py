from django.contrib import admin

from .models import Folder, Label, List, Note

admin.site.register(Folder)
admin.site.register(Label)
admin.site.register(List)
admin.site.register(Note)
