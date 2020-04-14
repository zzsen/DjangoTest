# goods/filters.py

import django_filters

from .models import Books


class BooksFilter(django_filters.rest_framework.FilterSet):
    '''
    书本过滤的类
    '''
    #两个参数，name是要过滤的字段，lookup是执行的行为，‘小与等于本店价格’
    #最新版本的django-filter  参数名字已经由name 更改为field_name
    price_min = django_filters.NumberFilter(field_name="shop_price", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name="shop_price", lookup_expr='lte')
    ordering = django_filters.OrderingFilter(fields=('sold_num', 'add_time'), field_labels={'sold_num': '销量', 'add_time': '添加时间'})

    class Meta:
        model = Books
        fields = ['price_min', 'price_max']