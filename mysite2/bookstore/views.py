
# Create your views here.
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

        try:
            models.Book.objects.create(
                title=title,
                #author=author,
                price=price,
                pub_house=pub_house,
                market_price=market_price
            )
        except Exception as e:
            print("添加图书失败：", e)
            return HttpResponse("图书添加失败！")
        # 如果没有异常，说明添加成功
        return HttpResponse("图书添加成功！")
    return render(request, "bookstore/add_book.html")

def show_all_books(request):
    books = models.Book.objects.all()
    #for book in books:
    #    print(book)
    #return HttpResponse("图书列表：<br>" + "<br>".join([str(book) for book in books]))
    return render(request, "bookstore/list.html", {"books": books})
def delete_book(request, book_id):
    try:
        book = models.Book.objects.get(id=book_id)
        book.delete()
    except Exception as e:
        print("删除图书失败：", e)
        return HttpResponse("图书删除失败！")
    
    return HttpResponse("图书删除成功！")
def edit_book(request, book_id):
    try:
        book = models.Book.objects.get(id=book_id)
    except Exception as e:
        print("未找到图书：", e)
        return HttpResponse("未找到要修改的图书！")

    if request.method == "GET":
        return render(request, "bookstore/edit_book.html", {"book": book})
    elif request.method == "POST":
        title = request.POST.get("title")
        market_price = request.POST.get("market_price")
        try:
            book.title = title
            book.market_price = market_price
            book.save()
        except Exception as e:
            print("更新图书失败：", e)
            return HttpResponse("图书更新失败！")
        return HttpResponse("图书更新成功！")



