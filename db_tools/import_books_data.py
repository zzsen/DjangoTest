import sys
import os

#获取当前文件的路径（运行脚本）
pwd = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
#获取项目的跟目录
sys.path.append(pwd)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoVue.settings")

#独立使用django的model
import django
django.setup()

from books.models import Books, BooksCategory, BooksImage

from db_tools.data.product_data import row_data

for books_detail in row_data:
    books = Books()
    books.name = books_detail["name"]
    #前端中是“￥232”，数据库中是float类型，所以要替换掉
    books.market_price = float(int(books_detail["market_price"].replace("￥", "").replace("元", "")))
    books.shop_price = float(int(books_detail["sale_price"].replace("￥", "").replace("元", "")))
    books.books_brief = books_detail["desc"] if books_detail["desc"] is not None else ""
    books.books_desc = books_detail["books_desc"] if books_detail["books_desc"] is not None else ""
    # 取第一张作为封面图
    books.books_front_image = books_detail["images"][0] if books_detail["images"] else ""
    #取最后一个
    category_name = books_detail["categorys"][-1]
    # 取出当前子类对应的BooksCategory对象，filter没有匹配的会返回空数组，不会抛异常。
    category = BooksCategory.objects.filter(name=category_name)
    if category:
        books.category = category[0]
    books.save()

    for books_image in books_detail["images"]:
        books_image_instance = BooksImage()
        books_image_instance.image = books_image
        books_image_instance.books = books
        books_image_instance.save()