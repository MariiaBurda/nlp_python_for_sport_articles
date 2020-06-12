from django.shortcuts import render
from .forms import ArticleForm
import re
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from football.settings import nlp


def analysis_form(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)

        if form.is_valid():
            text = form.cleaned_data['input_text']
            players, football_clubs, areas, dates = article_nlp(text)

            columns = ['PLAYERS', 'FOOTBALL CLUBS', 'AREAS', 'DATES']

            max_len_values = max(len(players), len(football_clubs), len(areas), len(dates))
            values_list = [players, football_clubs, areas, dates]
            rows = []

            for i in range(max_len_values):
                row_i = []
                for value in values_list:
                    row_i.append(value[i]) if len(value) > i else row_i.append('')
                rows.append(row_i)

            return render(request, 'football_analysis/result.html',
                          {
                              'columns': columns,
                              'rows': rows
                          }
                          )
    else:
        form = ArticleForm()
    return render(request, 'football_analysis/index.html', {'form': form})


def article_nlp(text):
    players = set()
    football_clubs = set()
    areas = set()
    dates = set()

    doc = nlp(text)

    for entity in doc.ents:
        if entity.label_ == 'PERSON':
            pattern = r'(([A-Z][A-Za-z]+)\s([A-Z][A-Za-z]+))'
            result = re.search(pattern, entity.text)
            if result:
                players.add(result.group(0))
        if entity.label_ == 'ORG':
            football_clubs.add(entity.text)
        if entity.label_ == 'GPE':
            areas.add(entity.text)
        if entity.label_ == 'TIME' or 'DATE':
            pattern_1 = r'^[tT]he\s\w+th\sof\s\w+,\s\d+'
            pattern_2 = r'^\w+\sthe\s\w+th,\s\d+'
            pattern_3 = r'^\w+\s\w+,*\s\d+'
            pattern_list = [pattern_1, pattern_2, pattern_3]
            for pattern in pattern_list:
                result = re.search(pattern, entity.text)
                if result:
                    dates.add(result.group(0))

    players = list(players)
    football_clubs = list(football_clubs)
    areas = list(areas)
    dates = list(dates)

    return players, football_clubs, areas, dates
