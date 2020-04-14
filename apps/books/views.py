# books/views.py

from rest_framework.views import APIView
from books.serializers import BooksSerializer, CategorySerializer
from .models import Books, BooksCategory
from .filters import BooksFilter
from rest_framework.response import Response
from rest_framework import generics, viewsets, mixins, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


class BooksPagination(PageNumberPagination):
    '''
    书本列表自定义分页
    '''
    #默认每页显示的个数
    page_size = 10
    #可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    #页码参数
    page_query_param = 'page'
    #最多能显示多少页
    max_page_size = 100


# class BooksListView(APIView):
#     '''
#     书本列表
#     '''
#     def get(self,request,format=None):
#         books = Books.objects.all()
#         books_serialzer = BooksSerializer(books,many=True)
#         return Response(books_serialzer.data)


class BooksListView(generics.ListAPIView):
    # 书本列表页
    pagination_class = BooksPagination    #分页
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BooksListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    #书本列表页
    # 这里必须要定义一个默认的排序,否则会报错
    queryset = Books.objects.all().order_by('id')
    # 分页
    pagination_class = BooksPagination
    serializer_class = BooksSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    # 设置filter的类为我们自定义的类
    filter_class = BooksFilter
    #搜索,=name表示精确搜索，也可以使用各种正则表达式
    search_fields = ('=name', 'books_brief')
    #排序
    ordering_fields = ('sold_num', 'add_time')


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    list:
        书本分类列表数据
    '''

    queryset = BooksCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer