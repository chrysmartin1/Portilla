
from .import views
from django.urls import path,include

urlpatterns = [
    path('',views.index,name='index'),
    # path('john/',views.trial,name='trial'),
    path('about/',views.about,name='about')
]