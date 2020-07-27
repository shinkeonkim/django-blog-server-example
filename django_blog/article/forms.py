from django import forms
from .models import Article, Images


class ArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=128)
    body = forms.CharField(max_length=245, label="설명글")

    class Meta:
        model = Article
        fields = ('title', 'body' )

        
class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')    
    class Meta:
        model = Images
        fields = ('image', )