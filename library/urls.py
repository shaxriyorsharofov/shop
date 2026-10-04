from django.urls import path
from .views import HomePageView, BookListView, BookCreateView, BookDetailView, BookDeleteView, BookUpdateView
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),   # <-- asosiy sahifa
    path("book-list/", BookListView.as_view(), name="list"),
    path("create-book/", BookCreateView.as_view(), name="create_book"),
    path("detail-book/<int:pk>/", BookDetailView.as_view(), name="detail"),
    path("delete-book/<int:pk>/", BookDeleteView.as_view(), name="delete"),
    path("update-book/<int:pk>/", BookUpdateView.as_view(), name="update"),
]

