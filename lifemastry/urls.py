from django.contrib import admin
from django.urls import path, include
from UserRegistrationForm.views import registration_view, registration_success, send_otp, result,header_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', registration_view, name='registration'),
    path('registration/success/', registration_success, name='registration_success'),
    path("send_otp/", send_otp, name="send_otp"),
    path('', include('UserRegistrationForm.urls')),  # Include your app's URLs
    path('header/', header_view, name='header_view'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
