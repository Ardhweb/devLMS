from django.urls import path
from .views import BorrowDetain,BorrowList

urlpatterns = [
  
    path('<int:pk>/', BorrowDetain.as_view(), name='borrows-detail'),
    path('', BorrowList.as_view(), name='borrows-list'),
]
