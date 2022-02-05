from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, ScopeRelation

class ScopeRelationInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                counter += 1
            if counter > 1:
                raise ValidationError('Основным может быть только один раздел')
        if not counter:
            raise ValidationError('Укажите основной раздел')
        return super().clean()


class ScopeRelationInline(admin.TabularInline):
    model = ScopeRelation
    formset = ScopeRelationInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeRelationInline]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass
