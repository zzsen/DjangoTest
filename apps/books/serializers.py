# goods/serializers.py

from rest_framework import serializers
from .models import Books,BooksCategory

#Serializer实现书本列表页
# class BooksSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True,max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_image = serializers.ImageField()

class CategorySerializer3(serializers.ModelSerializer):
    # 三级分类
    class Meta:
        model = BooksCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    # 二级分类
    #在parent_category字段中定义的related_name="sub_cat"
    sub_cat = CategorySerializer3(many=True)
    class Meta:
        model = BooksCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    # 书本一级类别序列化
    sub_cat = CategorySerializer2(many=True)
    class Meta:
        model = BooksCategory
        fields = "__all__"

#ModelSerializer实现书本列表页
class BooksSerializer(serializers.ModelSerializer):
    # 覆盖外键字段
    category = CategorySerializer()
    class Meta:
        model = Books
        fields = '__all__'