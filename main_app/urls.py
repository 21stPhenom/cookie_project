from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<str:book_hash>', views.book_detail, name='book-detail')
]