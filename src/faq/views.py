from django.shortcuts import render
from .models import Articles


# Create your views here.
def faq(request):
    if request.method == "POST":
        keyword = request.POST.get('keyword', None)
        articles = Articles.objects.filter(title__icontains=keyword)
        return render(request, 'faq_category.html', locals())
    return render(request, 'faq.html', locals())


def about(request):
    articles = Articles.objects.filter(article_category=0)
    category = "About"
    return render(request, 'faq_category.html', locals())


def safety(request):
    articles = Articles.objects.filter(article_category=1)
    category = "Safety & Security"
    return render(request, 'faq_category.html', locals())


def evaluation(request):
    articles = Articles.objects.filter(article_category=2)
    category = "Evaluation"
    return render(request, 'faq_category.html', locals())


def rules(request):
    articles = Articles.objects.filter(article_category=3)
    category = "Rules"
    return render(request, 'faq_category.html', locals())


def faqs(request, id):
    try:
        article = Articles.objects.get(id=id)
    except:
        return render(request, 'error.html')
    return render(request, 'faqs.html', locals())
