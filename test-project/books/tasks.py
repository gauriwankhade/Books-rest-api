from celery import shared_task,Celery
from django.core.files.base import ContentFile
import urllib.request
from .models import Book

@shared_task
def upadte_download():
    # book = Book.objects.get(pk=id)
    # url = book.url
    # my_request = urllib.request.urlopen(url)
    # my_HTML = my_request.read().decode("utf8")
        
    # updated_file = ContentFile(my_HTML)
    # updated_file.name = "{book_name}.html".format(book_name=book.name)

    # book.downloaded_file = updated_file
    # book.is_downloaded = True
    # print('------>',book.is_downloaded)
    # book.save()
    print("helllo world")

    