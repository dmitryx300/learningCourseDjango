from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
author = {'Имя': 'Иван', 'Отчество': 'Петрович', 'Фамилия': 'Иванов',
          'телефон': '8-923-600-01-02', 'email': 'vasya@mail.ru'}

def home(request):
    text = """<h1>"Изучаем Django"</h1>
            <strong>Автор</strong>: <i>Иванов И.П.</i>"""
    return HttpResponse(text)

def about(request):

    # text = f"""Имя: <b>{author['Имя']}</b><br>
    # Отчество: <b>{author['Отчество']}</b><br>
    # Фамилия: <b>{author['Фамилия']}</b><br>
    # телефон: <b>{author['телефон']}</b><br>
    # email: <b>{author['email']}</b>"""
    text = str()
    for key, value in author.items():
        text += str(key) + ': <b>' + str(value) + '</b><br>'
    return HttpResponse(text)


items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]

def get_item(request, id):
    for item in items:
        if item['id'] == id:
            text = f"""
            <h2>Имя: {item['name']}</h2>
            <p>quantity: {item['quantity']}</p>
            """
            return HttpResponse(text)
    return(HttpResponseNotFound(f'Item with id={id} not found'))

def items_list(request):
    """<ol>
    <li></li>
    <li> </li>
    <li> </li>
    <li> </li>
    <li> </li>
    </ol>"""
    result = "<h2>Список товаров</h2><ol>"
    for item in items:
        result +=f"<li>{item['name']}</li>"
    result += '</ol>'
    return HttpResponse(result)