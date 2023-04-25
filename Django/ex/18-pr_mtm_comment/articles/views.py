from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Comment, Emote
from .forms import ArticleForm, CommentForm



EMOTIONS = [
    {'label': '재밌어요', 'value': 1, 'icon': 'star', 'color': 'warning'},
    {'label': '싫어요', 'value': 2, 'icon': 'heartbreak', 'color': 'secondary'},
    {'label': '화나요', 'value': 3, 'icon': 'emoji-angry', 'color': 'danger'},
]

def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    emotions = []
    for emotion in EMOTIONS:
        label = emotion['label']
        value = emotion['value']
        icon = emotion['icon']
        color = emotion['color']
        count = Emote.objects.filter(article=article, emotion=value).count()
        if request.user.is_authenticated:
            exist = Emote.objects.filter(article=article, emotion=value, user=request.user)
        else:
            exist = None
        emotions.append(
            {
                'label': label,
                'value': value,
                'icon': icon,
                'color': color,
                'count': count,
                'exist': exist,
            }
        )

    comments = article.comment_set.all()
    comment_form = CommentForm()
    context = {
        'emotions': emotions,
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)



@login_required
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article_pk=article.pk)

    else:
        form = ArticleForm()

    context = {
        'form': form,
    }

    return render(request, 'articles/create.html', context)


@login_required
def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.article = article
        comment.save()

    return redirect('articles:detail', article.pk)


@login_required
def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()

    return redirect('articles:detail', article_pk)


@login_required
def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect('articles:detail', article_pk=article.pk)

    
@login_required
def like_comment(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if comment.like_users.filter(pk=request.user.pk).exists():
        comment.like_users.remove(request.user)
    else:
        comment.like_users.add(request.user)
    return redirect('articles:detail', article_pk)

@login_required
def emotes(request, article_pk, emotion):
    article = Article.objects.get(pk=article_pk)
    filter_query = Emote.objects.filter(
        article=article,
        user=request.user,
        emotion=emotion,
    )
    if filter_query.exists():
        filter_query.delete()
    else:
        Emote.objects.create(article=article, user=request.user, emotion=emotion)

    return redirect('articles:detail', article_pk)