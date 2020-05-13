from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='homepage'), #home è la function inside views.py chiamata
    path('count/',views.count, name='count'),
    path('about/',views.aboutpage, name='about'),
]


''' OLD
urlpatterns = [
    path('admin/', admin.site.urls),
]'''