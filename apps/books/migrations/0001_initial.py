# Generated by Django 3.0 on 2020-03-29 10:04

import DjangoUeditor.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('books_sn', models.CharField(default='', max_length=50, verbose_name='书本唯一货号')),
                ('name', models.CharField(max_length=100, verbose_name='书本名')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击数')),
                ('sold_num', models.IntegerField(default=0, verbose_name='书本销售量')),
                ('fav_num', models.IntegerField(default=0, verbose_name='收藏数')),
                ('books_num', models.IntegerField(default=0, verbose_name='库存数')),
                ('market_price', models.FloatField(default=0, verbose_name='市场价格')),
                ('shop_price', models.FloatField(default=0, verbose_name='本店价格')),
                ('books_brief', models.TextField(max_length=500, verbose_name='书本简短描述')),
                ('books_desc', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
                ('ship_free', models.BooleanField(default=True, verbose_name='是否承担运费')),
                ('books_front_image', models.ImageField(blank=True, null=True, upload_to='books/images/', verbose_name='封面图')),
                ('is_new', models.BooleanField(default=False, verbose_name='是否新品')),
                ('is_hot', models.BooleanField(default=False, help_text='是否热销', verbose_name='是否热销')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '书本信息',
                'verbose_name_plural': '书本信息',
            },
        ),
        migrations.CreateModel(
            name='BooksCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='类别名', max_length=30, verbose_name='类别名')),
                ('code', models.CharField(default='', help_text='类别code', max_length=30, verbose_name='类别code')),
                ('desc', models.TextField(default='', help_text='类别描述', verbose_name='类别描述')),
                ('category_type', models.IntegerField(choices=[(1, '一级类目'), (2, '二级类目'), (3, '三级类目')], help_text='类目级别', verbose_name='类目级别')),
                ('is_tab', models.BooleanField(default=False, help_text='是否导航', verbose_name='是否导航')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('parent_category', models.ForeignKey(blank=True, help_text='父目录', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_cat', to='books.BooksCategory', verbose_name='父类目级别')),
            ],
            options={
                'verbose_name': '书本类别',
                'verbose_name_plural': '书本类别',
            },
        ),
        migrations.CreateModel(
            name='HotSearchWords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(default='', max_length=20, verbose_name='热搜词')),
                ('index', models.IntegerField(default=0, verbose_name='排序')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '热搜排行',
                'verbose_name_plural': '热搜排行',
            },
        ),
        migrations.CreateModel(
            name='IndexAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books.Books')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='books.BooksCategory', verbose_name='书本类目')),
            ],
            options={
                'verbose_name': '首页广告',
                'verbose_name_plural': '首页广告',
            },
        ),
        migrations.CreateModel(
            name='BooksImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='图片')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='books.Books', verbose_name='书本')),
            ],
            options={
                'verbose_name': '书本轮播',
                'verbose_name_plural': '书本轮播',
            },
        ),
        migrations.CreateModel(
            name='BooksCategoryBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='品牌名', max_length=30, verbose_name='品牌名')),
                ('desc', models.TextField(default='', help_text='品牌描述', max_length=200, verbose_name='品牌描述')),
                ('image', models.ImageField(max_length=200, upload_to='brands/')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='books.BooksCategory', verbose_name='书本类目')),
            ],
            options={
                'verbose_name': '宣传品牌',
                'verbose_name_plural': '宣传品牌',
                'db_table': 'books_booksbrand',
            },
        ),
        migrations.AddField(
            model_name='books',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.BooksCategory', verbose_name='书本类目'),
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='banner', verbose_name='轮播图片')),
                ('index', models.IntegerField(default=0, verbose_name='轮播顺序')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Books', verbose_name='书本')),
            ],
            options={
                'verbose_name': '首页轮播',
                'verbose_name_plural': '首页轮播',
            },
        ),
    ]
