from django_filters import FilterSet, CharFilter
from .models import Post

# Создаем свой набор фильтров для модели Post.

class PostFilter(FilterSet):
    dateCreation = DateFilter(
        lookup_expr='gt',
        widget=django.forms.DateInput(
            attrs={
                'type': 'date'
            }
        )
    )

   class Meta:
       model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {
           'title': ['icontains']
       }




