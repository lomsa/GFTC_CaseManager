# -*- coding: utf-8 -*-
from django.db import models


class MSG(models.Model):
    file_name = models.CharField(max_length=300, blank=True)
    mt = models.CharField(max_length=300, blank=True)
    day = models.CharField(max_length=300, blank=True)
    time = models.CharField(max_length=300, blank=True)
    bic = models.CharField(max_length=300, blank=True)
    io = models.CharField(max_length=300, blank=True)

    def __unicode__(self):
        return u'%s' % (self.file_name)

    class Meta:
        verbose_name = '1. მესიჯი'
        verbose_name_plural = '1. მესიჯი'


class MSG195(models.Model):
    sender = models.CharField(max_length=300)
    reciver = models.CharField(max_length=300)
    reference20 = models.CharField(max_length=300)
    referance21 = models.CharField(max_length=300)
    name75 = models.CharField(max_length=300)
    comment77a = models.CharField(max_length=300)
    comment70 = models.CharField(max_length=300)
    description79 = models.TextField(max_length=300)
    data11a = models.CharField(max_length=300)
    input_output = models.CharField(max_length=300)
    kay = models.ForeignKey(MSG)

    def __unicode__(self):
        return u'%s' % (self.sender, self.reciver)

    class Meta:
        verbose_name = 'მესიჯი 195'
        verbose_name_plural = 'მესიჯი 195'


class MSG199(models.Model):
        sender = models.CharField(max_length=300)
        reciver = models.CharField(max_length=300)
        reference20 = models.CharField(max_length=300)
        referance21 = models.CharField(max_length=300)
        field_79 = models.TextField(max_length=300)
        input_output = models.CharField(max_length=300)

        def __unicode__(self):
            return u'%s' % (self.sender, self.reciver)

        class Meta:
            verbose_name = 'მესიჯი 199'
            verbose_name_plural = 'მესიჯი 199'

class MSG196(models.Model):
        sender = models.CharField(max_length=300)
        reciver = models.CharField(max_length=300)
        reference20 = models.CharField(max_length=300)
        referance21 = models.CharField(max_length=300)
        field_76 = models.TextField(max_length=300)
        field_77a = models.TextField(max_length=300)
        date_11 = models.CharField(max_length=300)
        field_79 = models.TextField(max_length=300)
        input_output = models.CharField(max_length=300)

        def __unicode__(self):
            return u'%s' % (self.sender, self.reciver)

        class Meta:
            verbose_name = 'მესიჯი 196'
            verbose_name_plural = 'მესიჯი 196'

class MSG192(models.Model):
          sender = models.CharField(max_length=300)
          reciver = models.CharField(max_length=300)
          reference20 = models.CharField(max_length=300)
          referance21 = models.CharField(max_length=300)
          date_11 = models.CharField(max_length=300)
          name79 = models.TextField(max_length=300)
          input_output = models.CharField(max_length=300)

          def __unicode__(self):
                return u'%s' % (self.sender, self.reciver)

          class Meta:
               verbose_name = 'მესიჯი 192'
               verbose_name_plural = 'მესიჯი 192'
