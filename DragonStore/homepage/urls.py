from django.urls import path

from .views import index, types_of_dragons, buy_dragon
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('types_of_dragons/', types_of_dragons, name='types_of_dragons'),
    path('buy/<int:dragon_id>>', buy_dragon, name='form_buyer'),
    path('', index, name='index'),
]