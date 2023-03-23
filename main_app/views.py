from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View

from main_app.models import Book

# Create your views here.
class Index(View):

    def get(self, request):
        request.session['user_ip'] = request.META.get("REMOTE_ADDR")
        request.session['random_cookie'] = "this is a test cookie"
        
        context = {
            'user_ip': request.session['user_ip']
        }
        return render(request, 'main_app/index.html', context=context)

class BookDetail(View):
    manager = Book.objects

    def get_object(self, hash):
        try:
            book = self.manager.get(book_hash=hash)
        except Book.DoesNotExist:
            raise Http404

        return book

    def get(self, request, book_hash):
        
        book = self.get_object(book_hash)
        print(request.session['new_cookie'])
        context = {
            "book": book
        }
        return render(request, 'main_app/book.html', context=context)

index = Index.as_view()
book_detail = BookDetail.as_view()