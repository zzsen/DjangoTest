# goods/adminx.py

import xadmin
from .models import Books, BooksCategory, BooksImage, BooksCategoryBrand, Banner, HotSearchWords
from .models import IndexAd


class BooksAdmin(object):
    #显示的列
    list_display = ["name", "click_num", "sold_num", "fav_num", "goods_num", "market_price",
                    "shop_price", "goods_brief", "goods_desc", "is_new", "is_hot", "add_time"]
    #可以搜索的字段
    search_fields = ['name', ]
    #列表页可以直接编辑的
    list_editable = ["is_hot", ]
    #过滤器
    list_filter = ["name", "click_num", "sold_num", "fav_num", "goods_num", "market_price",
                   "shop_price", "is_new", "is_hot", "add_time", "category__name"]
    #富文本编辑器
    style_fields = {"goods_desc": "ueditor"}

    #在添加书本的时候可以添加书本图片
    class BooksImagesInline(object):
        model = BooksImage
        exclude = ["add_time"]
        extra = 1
        style = 'tab'

    inlines = [BooksImagesInline]


class BooksCategoryAdmin(object):
    list_display = ["name", "category_type", "parent_category", "add_time"]
    list_filter = ["category_type", "parent_category", "name"]
    search_fields = ['name', ]


class BooksBrandAdmin(object):
    list_display = ["category", "image", "name", "desc"]

    def get_context(self):
        context = super(BooksBrandAdmin, self).get_context()
        if 'form' in context:
            context['form'].fields['category'].queryset = BooksCategory.objects.filter(category_type=1)
        return context


class BannerBooksAdmin(object):
    list_display = ["goods", "image", "index"]


class HotSearchAdmin(object):
    list_display = ["keywords", "index", "add_time"]


class IndexAdAdmin(object):
    list_display = ["category", "goods"]


xadmin.site.register(Books, BooksAdmin)
xadmin.site.register(BooksCategory, BooksCategoryAdmin)
xadmin.site.register(Banner, BannerBooksAdmin)
xadmin.site.register(BooksCategoryBrand, BooksBrandAdmin)

xadmin.site.register(HotSearchWords, HotSearchAdmin)
xadmin.site.register(IndexAd, IndexAdAdmin)