from django import forms


class NumbersSumForm(forms.Form):
    number_one = forms.IntegerField(required=True)
    number_two = forms.IntegerField(required=True)
    number_sum = forms.IntegerField(required=False)
