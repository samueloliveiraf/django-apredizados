from django.contrib import admin
from django.contrib.auth.models import User, Group


admin.site.unregister(
    [
        User,
        Group,
    ]
)


admin.site.site_header = 'TodoApp Login'

admin.site.site_title = 'Admin TodoApp'

admin.site.index_title = 'Admin TodoApp Aplicações'

