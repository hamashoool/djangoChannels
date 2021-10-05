from django.urls import path

from noties import views as v

urlpatterns = [
    path('', v.home, name='home'),
    path('like/<post_id>/', v.like, name='like'),
]
