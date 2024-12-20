from django.urls import path, include

urlpatterns = [
    path('authors/', include('api_drf.author.urls')),  # Include app1 API URLs
    path('books/', include('api_drf.books.urls')),
    path('borrows/', include('api_drf.borrow.urls')),
    path('reports/', include('api_drf.reports.urls')),
]
