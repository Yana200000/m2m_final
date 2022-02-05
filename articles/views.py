from django.views.generic import ListView

from articles.models import Article, ScopeRelation


class ArticleListView(ListView):
    template_name = 'articles/news.html'
    model = Article
    ordering = '-published_at'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_list = []
        scope_list = []

        for article in context['object_list']:
            for scope in ScopeRelation.objects.filter(article=article).all():
                scope_list.append({'topic': scope.scope.topic, 'is_main': scope.is_main})
            article.scopes = sorted(scope_list, key=lambda x: x['is_main'], reverse=True)
            article_list.append(article)
            scope_list.clear()
        context['object_list'] = article_list
        return context
