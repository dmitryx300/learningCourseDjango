from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from MainApp.models import Item

# Create your views here.
author = {'Имя': 'Иван', 'Фамилия': 'Петрович', 'Отчество': 'Иванов',
          'Телефон': '8-923-600-01-02', 'email': 'vasya@mail.ru'}


# items = [
#    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
#    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
#    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
#    {"id": 7, "name": "Картофель фри", "quantity": 0},
#    {"id": 8, "name": "Кепка", "quantity": 124},
# ]
#menu = ['Home', 'Items', 'About']

def home(request):
    contex = {
        'name': 'Петров Николай Иванович',
        'email': 'mail@mail.ru',
        'title': 'Home page'
    }
    return render(request, 'index.html', contex)


def about(request):

    # text = str()
    # for key, value in author.items():
    #     text += str(key) + ': <b>' + str(value) + '</b><br>'
    #return HttpResponse(text)
    contex={
        'author': author,
        'title': 'About author'
    }
    return render(request, 'about.html', contex)

def get_item(request, id):
    # for item in items:
    #     if item['id'] == id:
    #     #     text = f"""
    #     #     <h2>Имя: {item['name']}</h2>
    #     #     <p>quantity: {item['quantity']}</p>
    #     #     <a href='/items'> Назад </a>
    #     #     """
    #     #     return HttpResponse(text)
    #         context = {
    #             'item': item,
    #             'menu': menu,
    #             'title': 'Item page'
    #         }
    try:
        item = Item.objects.get(id=id)
    except ObjectDoesNotExist:
        return(HttpResponseNotFound(f'Item with id={id} not found'))
    context = {
        'item': item,
        'title': 'Item page'
    }
    return render(request, 'item-page.html', context)


def items_list(request):
    # result = "<h2>Список товаров</h2><ol>"
    # for item in items:
    #     result +=f"<li><a href='/item/{item['id']}'>{item['name']}</a></li>"
    # result += '</ol>'
    #return HttpResponse(result)
    context = {
        'items': Item.objects.all(),
        'title': 'Items main'
    }
    return render(request, 'items-list.html', context)