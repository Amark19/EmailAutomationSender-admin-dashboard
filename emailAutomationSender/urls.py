from django.contrib import admin
from django.urls import path,include


admin.site.site_header = "Login to Email Automation dashboard"
admin.site.site_title = "Welcome to dashboard"
admin.site.index_title = "Welcome to this portal"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("emailSend.urls")),
]