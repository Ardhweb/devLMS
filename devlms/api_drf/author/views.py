#CBV
from .serializers import AuthorSerializer
from author.models import Author
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

class AuthorList(APIView):
    """
    List of all authors.
    GET /authors/
    """
    @swagger_auto_schema(
        operation_description="This endpoint returns a list of all authors objects from records that we have.",
        responses={200: "Return all authors list via GET Method."}
    )
    def get(self, request, format=None):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="This endpoint we can create new author entry to database or just create an new author.",
        responses={200: "This will return latest created author detials in response."}
    )
    def post(self, request, format=None):
      serializer = AuthorSerializer(data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetail(APIView):

    def get_object(self, pk):
        try:
            return  Author.objects.get(pk=pk)
        except  Author.DoesNotExist:
            raise Http404
    @swagger_auto_schema(
        operation_description="For Get any specific or you faviourete author detials you need there pk or id from records.",
        responses={200: "Using pk it will retunr spcific author details objects in response."}
    )
    def get(self, request, pk, format=None):
        author = self.get_object(pk)
        serializer =  AuthorSerializer(author)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        operation_description="This endpoint just updating any detials or data of any sepcifci author that we got using pk -value and we can pass formadata which author date filds value we needs to update like author name e.e name : Json Ned .etc",
        responses={200: "Return Latest update spcific author data"}
    )
    def put(self, request, pk, format=None):
        author = self.get_object(pk)
        serializer =  AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        operation_description="This endpointwe just eliemant or remove any author from records using there pk-value",
        responses={200: "Return deleted author data."}
    )
    def delete(self, request, pk, format=None):
        deleted_authors = []
        author = self.get_object(pk)
        deleted_authors.append(author)
        author.delete()
        #return Response(status=status.HTTP_204_NO_CONTENT,)
        return Response(
        {
            "message": "Author deleted successfully",
            "deleted_author": {
                "id": author.id,
                "name": author.name,  # Adjust according to your model's fields
                # Add other fields as necessary
            }
        },
        status=status.HTTP_204_NO_CONTENT
    )