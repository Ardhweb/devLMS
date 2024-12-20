from rest_framework import serializers
from book.models import Book
from author.models import Author
'''
class BookSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        view_name='author-detail',  # Refers to the Author detail view
        queryset=Author.objects.all()
    )
    class Meta:
        model = Book
        fields = ['id','title','author','isbn','available_copies']'''


class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ['id','title','author','isbn','available_copies']

