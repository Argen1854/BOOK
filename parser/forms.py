from django.forms import forms
from . import parser, parser_manga, models
from django import forms


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('ANIME', 'ANIME'),
        ('MANGA', 'MANGA'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]

    def parse_data(self):
        if self.data['media_type'] == 'ANIME':
            anime_parser = parser.parser()
            for i in anime_parser:
                models.Film.objects.create(**i)
        elif self.data['media_type'] == 'MANGA':
            manga_parser = parser_manga.parser()
            for i in manga_parser:
                models.Manga.objects.create(**i)

        