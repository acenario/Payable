from django.contrib import admin
from django.contrib.auth import get_user_model

class SignUpAdmin(admin.ModelAdmin):
    class Meta:
        model = get_user_model()
admin.site.register(get_user_model(), SignUpAdmin)