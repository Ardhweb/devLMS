from celery import shared_task
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
from .utils import gd
import sys

# Set up logging
logger = logging.getLogger(__name__)

@shared_task
def generate_report():
    """
    Simulate a report generation task. This can be replaced with actual logic for report generation.
    """
    gd()
    # Fetch counts
   
    logger.info(f"JSON file  created successfully in the same folder.")
        # Simulate long-running task
    logger.info("Simulating report generation time...")
    time.sleep(5)  # Simulate long processing time    logger.info("Report generated successfully!")    return f"Report generated and saved as {filename}"

  