
import time
from author.models import Author
from book.models import Book
from brecord.models import BorrowRecord
from django.http import Http404
import datetime
import os
import json
import logging
import time

def gd():
    total_authors = Author.objects.count()
    total_books = Book.objects.count()
    total_borrowed_books = BorrowRecord.objects.filter(return_date__isnull=True).count()
    print(f"Authors: {total_authors} \n Books :{total_books} \n Borrowed Books:{total_borrowed_books}")
    data = {
        'Total number of authors':total_authors,
        'Total number of books':total_books,
        'Total books currently borrowed':total_borrowed_books
    }
    today = datetime.date.today()
    filename = today.strftime("%Y%m%d") + ".json"
    # Use relative path to go two levels up to devlsm (from devlms/api_drf/reports)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'reports', filename)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
    print(f"JSON file '{filename}' created successfully in the 'reports' folder.")
       
   