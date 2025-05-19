from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def add_book(request):
    if request.method == "GET":
        return render(request, "bookstore/add_book.html")
    # POST请求处理
    elif request.method == "POST":
        title = request.POST.get("title")
        #author = request.POST.get("author")
        price = request.POST.get("price")
        pub_house = request.POST.get("pub_house")
        market_price = request.POST.get("market_price")

        book = models.Book(
            title=title,
            #author=author,
            price=price,
            pub_house=pub_house,
            market_price=market_price
        )
        book.save()
        return HttpResponse("图书添加成功！")
    return render(request, "bookstore/add_book.html")
