from django.db import models
from django.core.exceptions import ValidationError

class Word(models.Model):
    name = models.CharField(max_length=50)

class Language(models.Model):
    name = models.CharField(max_length=50)

class Sentence(models.Model):
    words = models.ManyToManyField(Word)
    language = models.ForeignKey(Language)

    def clean(self):
        for word in self.words.all():
            if word.language_id != self.language_id:
                raise ValidationError('One of the words has a false language')