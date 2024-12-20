#CBV
from .serializers import BookSerializer
from ..author.serializers import AuthorSerializer
from book.models import Book
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

class BookList(APIView):
    """
    List of all books.
    GET /books/
    """
    @swagger_auto_schema(
        operation_description="This endpoint returns a list of all books objects.",
        responses={200: "Books Related Objects"}
    )
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="This endpoint returns create a new of book objects.",
        responses={200: "This will return latest new created Book object in response. "}
    )
    def post(self, request, format=None):
      serializer = BookSerializer(data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetail(APIView):

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer =  BookSerializer(book)
        return Response(serializer.data)
    
    @swagger_auto_schema(
    operation_description="This endpoint  we will update any specific book data using there pk-value or id as pamater.",
    responses={200: "This will return latest new update exisitng book data into response "}
    )
    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer =  BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
    operation_description="This endpoint  we will remove or delete any specific book from database records using there pk-value or id as pamater.",
    responses={200: "This will return with current book deleting instance data  into response "}
    )
    def delete(self, request, pk, format=None):
        deleted_books = []
        book = self.get_object(pk)
        deleted_books.append(book)
        author_data = {"id":book.author.id,'name': book.author.name} if book.author else None
        book.delete()
        #return Response(status=status.HTTP_204_NO_CONTENT,)
        return Response(
        {
            "message": "Book is deleted successfully.Only Book has been deletd not removed the author.",
            "deleted_books": {
                "id": book.id,
                "title": book.title,  # Adjust according to your model's fields
                "isbn":book.isbn,
                "available_copies":book.available_copies,
                "author":author_data
            }
        },
        status=status.HTTP_204_NO_CONTENT
    )
    