from .models import Images, Article
from .forms import ImageForm, ArticleForm
from django.shortcuts import redirect, render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext

@login_required
def upload_article(request):
    ImageFormSet = modelformset_factory(Images, form = ImageForm , extra = 1)

    if request.method == "POST":
        form = ArticleForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset = Images.objects.none())
        if form.is_valid() and formset.is_valid():
            article = form.save(commit=False)
            article.publisher = request.user
            article.save()
            for form in formset.cleaned_data:
                image = form['image']
                photo = Images(article=article, image=image)
                photo.save()
            messages.success(request,
                             "Posted!")
            return redirect("/")

    else:
        form = ArticleForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'upload_article.html',
                    {'ArticleForm': form, 'formset': formset})


def show_articles(request):
    articles = Article.objects.all()[::-1]
    paginator = Paginator(articles, 10)
    page= request.GET.get('page')
    if page == "" or page == None:
        page = 1
    articles_page = paginator.get_page(page)
    start = max(int(page)-5, 1)
    end = min(int(page)+5, paginator.num_pages)

    for i in articles:
        i.images = Images.objects.all().filter(article = i)
        
    return render(request, 'show_articles.html', {'articles':articles, 'articles_page' : articles_page, 'range' : [i for i in range(start, end+1)]})