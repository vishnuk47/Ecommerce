from django.urls import path
from . import views

urlpatterns=[
    path('home',views.home,name='home'),
    path('page',views.page,name='page'),
    path('about',views.about,name="about"),
    path('sample',views.sample),
    path('css',views.cssexa),
    path('new',views.newpage),
    path('pad',views.pad),
    path('grid',views.grid),
    path('grid1',views.grid1),
    path('boot',views.boot),
    path('boots',views.boots),
    path('baabtrapage',views.baabtra),
    path('bootstrap',views.boo)
]