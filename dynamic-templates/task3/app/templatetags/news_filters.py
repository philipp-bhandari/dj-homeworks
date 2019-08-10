from django import template
import time
import datetime

register = template.Library()


@register.filter
def format_date(value):
    value = int(value)
    minutes = round((time.time() - value) / 60)
    hours = round(minutes / 60)
    if minutes < 10:
        return 'Только что'
    if hours < 24:
        return f'{hours} часов назад'
    return datetime.datetime.fromtimestamp(value)


@register.filter
def format_score(value, default):
    try:
        value = int(value)
    except ValueError:
        return default
    if value < -5:
        return 'всё плохо'
    if -5 < value < 5:
        return 'нейтрально'
    if value > 5:
        return 'хорошо'


@register.filter
def format_num_comments(value):
    value = int(value)
    if value is 0:
        return 'оставьте комментарий'
    if 0 < value < 50:
        return value
    if value >= 50:
        return '50+'


@register.filter
def format_selftext(value, count):
    words_list = value.split(' ')
    return ' '.join(words_list[0:count]) + ' ... ' + ' '.join(words_list[-5:])
