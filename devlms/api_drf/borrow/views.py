#CBV
from .serializers import BorrowSerializer
from ..books.serializers import BookSerializer
from brecord.models import BorrowRecord
from book.models import Book
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema



class BorrowList(APIView):
    
    def get(self, request, format=None):
        borrows = BorrowRecord.objects.all()
        serializer = BorrowSerializer(borrows, many=True)
        return Response(serializer.data)
    @swagger_auto_schema(
    operation_description="This endpoint  will create a new borrow record and also updating/decreasing the available_copies value from books which we currentlry borrowing via this.",
    responses={200: "This will return latest borrow record data in response "}
    )
    def post(self, request, format=None):
        serializer = BorrowSerializer(data=request.data)
        book_instance = Book.objects.get(id=request.data['book'])
        print(request.data['book'])
        if serializer.is_valid():
            serializer.save()
            if request.data['book'] == [] or None:
                print('no book selcted')
            else:
                book_instance.available_copies -= 1  # Decrease the copies by 1
                book_instance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

class BorrowDetain(APIView):

    def get_object(self, pk):
        try:
            return BorrowRecord.objects.get(pk=pk)
        except BorrowRecord.DoesNotExist:
            raise Http404
    @swagger_auto_schema(
    operation_description="This endpoint  will updating a specific borrow record and also updating/increasing the available_copies value from books which we returningor we borrowd in past  for this we need to book and borrowrecord both pk or id as parameter.",
    responses={200: "This will return latest updated borrow record data in response with present retunr date . "}
    )
    def put(self, request, pk, format=None):
        borrows = self.get_object(pk)
        serializer =  BorrowSerializer(borrows, data=request.data)
        book_instance = Book.objects.get(id=borrows.book.pk)
        if serializer.is_valid():
            serializer.save()
            if borrows.book.pk == [] or None:
               print('no book selcted')
            else:
               book_instance.available_copies += 1  #Increase the copies by 1
               book_instance.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
    