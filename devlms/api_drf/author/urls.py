from django.urls import path
from .views import AuthorList, AuthorDetail

urlpatterns = [
    path('', AuthorList.as_view(), name='authors-list'),
    path('<int:pk>/', AuthorDetail.as_view(), name='authors-detail'),
]
