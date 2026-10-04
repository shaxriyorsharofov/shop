from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Book
from .forms import BookUpdateForm
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView


class HomePageView(TemplateView):
    template_name = 'index.html'


class BookListView(ListView):
    queryset = Book.objects.all()
    template_name = 'list_books.html'
    context_object_name = 'books'


# class BookListView(View):
#     def get(self, request):
#         books = Book.objects.all().order_by('-id')
#         return render (request, 'list_books.html',context = {'books':books})


from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Book


class BookCreateView(CreateView):
    model = Book
    fields = [
        'name',
        'desc',
        'price',
        'quantity',
        'author',
        'type_janr',
    ]
    template_name = 'create_book.html'
    success_url = reverse_lazy('list')  # yoki '/library/book-list/'
    
    
    
# class BookCreateView(View):
#     def post(self, request):
#         Book.objects.create(
#             name = request.POST.get('name'),
#             desc = request.POST.get('desc'),
#             price = request.POST.get('price'),
#             quantity = request.POST.get("quantity"),
#             author = request.POST.get('author'),
#             type_janr = request.POST.get('type_janr'),

#         )
#         return redirect ('/library/book-list')
    
#     def get(self, request):
#         return render(request, 'create_book.html')


class BookDetailView(DetailView):
    model = Book
    template_name = 'detail_book.html'
    context_object_name = 'book'
    lookup_field = 'pk'
# class BookDetailView(View):
#     def get(self, request, id):
#         book = Book.objects.get(id = id)
#         return render(request, 'detail_book.html', context={'book':book})



class BookDeleteView(DeleteView):
    model = Book
    template_name = 'delete_book.html'
    
    context_object_name = 'book'
    success_url = reverse_lazy('list')

# class BookDeleteView(View):
#     def get_object(self, id):
#         book = Book.objects.get(id = id)
#         return book
    
#     def get(self, request, id): 
#         book = self.get_object(id)
#         return render (request, 'delete_book.html', context={'book':book})

#     def post(self, request, id):
#         book = self.get_object(id)
#         book.delete()
#         return redirect('list')


class BookUpdateView(UpdateView):
    model = Book
    fields = [
        'name',
        'desc',
        'price',
        'quantity',
        'author',
        'type_janr',
    ]
    context_object_name = 'book'
    success_url = reverse_lazy('list')
    template_name = 'update_book.html'
    context_object_name = 'book'
    success_url = reverse_lazy('list')


# class BookUpdateView(View):
#     def get_object(self, id):
#         book = Book.objects.get(id = id)
#         return book
    
#     def get(self, request, id): 
#         book = self.get_object(id)
#         form = BookUpdateForm(instance = book)
#         return render (request, 'update_book.html', context={'form':form, 'book': book})
    
#     def post(self, request, id):
#         book = self.get_object(id)
#         form = BookUpdateForm(instance=book, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('detail', book.id)
            
            
            