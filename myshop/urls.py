from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^cart/', include('cart.urls', namespace='cart')),
    re_path(r'^orders/', include('orders.urls', namespace='orders')),
    re_path(r'^', include('shop.urls', namespace='shop')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
