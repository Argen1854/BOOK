from re import template
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, FormView
from . import parser, models, forms


class ParserFormView(FormView):
    template_name = 'parser/parser.html'
    form_class = forms.ParserForm

    def post(self, request, *args, ** kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parse_data()
            # return HttpResponse('sdfsa')
            return redirect(reverse("parserlistmanga"))
        else:
            return super(ParserFormView, self).post(request, *args, **kwargs)



class ParserList(ListView):
    template = "parser/film_list.html"
    queryset = models.Film.objects.all()

    def get_queryset(self):
        return super().get_queryset()

class ParserListManga(ListView):
    template = "parser/manga_list.html"
    queryset = models.Manga.objects.all()

    def get_queryset(self):
        return super().get_queryset()






