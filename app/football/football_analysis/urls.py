from django.urls import path

from .views import analysis_form


urlpatterns = [
    path('', analysis_form, name='article_analysis_url'),
]

