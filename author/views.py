from django.shortcuts import render
from services.author.logic import logic_select_author


# Create your views here.
def select_author(request, id_author):
    dict_with_data = logic_select_author(id_author)
    return render(request, 'author/select_author.html', dict_with_data)
