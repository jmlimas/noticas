# -*- coding: utf-8 -*-

import datetime

from django.db                         import models
from django.contrib.auth.models        import User

class Rubrica(models.Model):
    title = models.CharField(u'Título', max_length=255)
    slug = models.SlugField(u'URL SLug')

    def __unicode__(self):
        return unicode(self.title)

class Noticia(models.Model):
    is_published = models.BooleanField(u'Status', default=False)
    pub_date     = models.DateTimeField(u'Fecha de publicación', default=datetime.datetime.now)
    author       = models.ForeignKey(User, verbose_name=u"Autor")
    rubric       = models.ForeignKey(Rubrica, verbose_name=u"Rúbrica")
    title        = models.CharField(u'Título', max_length=500, default=u'')
    body         = models.TextField(u'Contenido')

    def __unicode__(self):
        return self.title

    class Meta(object):
        ordering = ['-pub_date']