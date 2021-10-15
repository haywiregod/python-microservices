from django.contrib import admin
from django.urls import path, include
# from prod
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
]
