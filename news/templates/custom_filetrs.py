from django import template


register = template.Library()


# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.


@register.filter()
def censor(value):

    wrong_words = ['редиска', 'суицид', 'ремень', 'война', 'иноагент']
    for i in wrong_words:
        if i.find(value):
            value = value.replace(i[1::], "*" * len(i))
    return f'{value.lower()}'