from django import forms

RANGE = 10
CHOICE_LIST = list(map(lambda x: (str(x), x), range(RANGE)))


class ChooseNumberForm(forms.Form):
    number = forms.ChoiceField(choices=CHOICE_LIST, label='Выберите число')
