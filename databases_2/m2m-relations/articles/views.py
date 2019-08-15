from django.views.generic import ListView

from articles.models import Article, ArticleScope


class ArticleListView(ListView):
    template_name = 'articles/news.html'
    model = Article
    ordering = '-published_at'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = []

        for article in context['object_list']:
            scopes_list = []

            for item in ArticleScope.objects.filter(article=article).all():
                scopes_list.append({'topic': item.scopes.topic, 'is_main': item.is_main})

            article.scopes_all = sorted(scopes_list, key=lambda x: x['topic'] if not x['is_main'] else 'a')

            object_list.append(article)

        context['object_list'] = object_list

        return context
