#CBV
from author.models import Author
from book.models import Book
from brecord.models import BorrowRecord
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import datetime
import os
import json
from devlms.tasks import generate_report
from devlms.utils import gd
class ReportList(APIView):

    def get(self, request, format=None):
        # Get the base directory (adjust as needed to reach your reports directory)
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 2 levels up
        reports_dir = os.path.join(base_dir, 'reports')
    
        # Get all the .json files in the reports directory
        try:
            files = [f for f in os.listdir(reports_dir) if f.endswith('.json')]
        except FileNotFoundError:
            return Response({'error': 'Reports directory not found.'}, status=404)
        
        if not files:
            return Response({'error': 'No reports found.'}, status=404)

        # Return the filenames as a response
        return Response({'report_files': files}, status=200)

        
    def post(self, request, format=None):
        #gd()
        generate_report.delay()
        return Response(status=status.HTTP_200_OK)
       

    # def post(self, request, format=None):
    #     total_authors = Author.objects.count()
    #     total_books = Book.objects.count()
    #     total_borrowed_books = BorrowRecord.objects.filter(return_date__isnull=True).count()
    #     print(f"Authors: {total_authors} \n Books :{total_books} \n Borrowed Books:{total_borrowed_books}")
    #     data = {
    #         'Total number of authors':total_authors,
    #         'Total number of books':total_books,
    #         'Total books currently borrowed':total_borrowed_books
    #     }
    #     today = datetime.date.today()
    #     filename = today.strftime("%Y%m%d") + ".json"
    #     # Use relative path to go two levels up to devlsm (from devlms/api_drf/reports)
    #     base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    #     file_path = os.path.join(base_dir, 'reports', filename)
    #     os.makedirs(os.path.dirname(file_path), exist_ok=True)
    #     try:
    #         with open(file_path, "w") as file:
    #             json.dump(data, file, indent=4)
    #         print(f"JSON file '{filename}' created successfully in the 'reports' folder.")
    #         return Response(f"JSON file '{filename}' created successfully in the 'reports' folder.",status=status.HTTP_200_OK)
    #     except PermissionError as e:
    #         print(f"Permission error: {e}")
    #         return Response(status=status.HTTP_403_FORBIDDEN)
    #     except Exception as e:
    #         print(f"An error occurred: {e}")
    #         return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR )
