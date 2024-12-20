from django.urls import path
from .views import BookList, BookDetail

urlpatterns = [
    path('', BookList.as_view(), name='books-list'),
    path('<int:pk>/', BookDetail.as_view(), name='books-detail'),
]
