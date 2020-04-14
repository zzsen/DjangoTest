# goods/view_base.py

from django.views.generic import View
from books.models import Books
from django.forms.models import model_to_dict
from django.http import JsonResponse
# ImageFieldFile 和add_time字段不能序列化,要用到django的serializers
from django.core import serializers
import json

class BooksListView(View):
    def get(self,request):
        #通过django的view实现书本列表页
        json_list = []
        #获取所有书本
        goods = Books.objects.all()
        # for good in goods:
        #     json_dict = {}
        #     #获取书本的每个字段，键值对形式
        #     json_dict['name'] = good.name
        #     json_dict['category'] = good.category.name
        #     json_dict['market_price'] = good.market_price
        #     json_list.append(json_dict)

        json_data = serializers.serialize('json',goods)
        json_data = json.loads(json_data)
        #In order to allow non-dict objects to be serialized set the safe parameter to False.
        return JsonResponse(json_data,safe=False)