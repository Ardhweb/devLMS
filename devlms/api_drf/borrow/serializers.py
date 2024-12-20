from rest_framework import serializers
from book.models import Book
from brecord.models import BorrowRecord

class BorrowSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    class Meta:
        model = BorrowRecord
        fields = ['id','book','borrowed_by','borrow_date','return_date']

