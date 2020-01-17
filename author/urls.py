from django.urls import path, include
from .views import select_author

urlpatterns = [
    path('select_author/page-<int:id_author>', select_author, name="select_author"),

]
