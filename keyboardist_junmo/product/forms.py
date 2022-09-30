from socket import fromshare
from django import forms

class ProductSearchForm(forms.Form):
    search_word = forms.CharField(label='',
                                  widget=forms.TextInput(attrs={'placeholder': '검색어를 입력하세요'}))