from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from enum import Enum

# Create your models here.

class sake(models.Model):
    #(#'~~'#)選択肢作成よろしく
    #============================================
        TODOHUKEN = (('大阪','大阪'),('京都','京都'))
        SEIHO = (('生', '生'), ('火入れ', '火入れ'))
        SYURUI =  (('大吟醸', '大吟醸'), ('吟醸', '吟醸'),('純米吟醸','純米吟醸'))
        KARASA =  (('辛さ１', '辛さ１'), ('辛さ', '辛さ２'))
    #=============================================

        name = models.CharField('銘柄',max_length=100,default='')                       #銘柄
        creater = models.CharField('蔵元',max_length=100, blank=True,default='')        #蔵元
        region = models.CharField('都道府県',max_length=100,choices = TODOHUKEN,blank=True)                             #地域 0:北海道 1:東北　2:関東 3:北陸　4:近畿 5:中国　6:四国 7九州
        created_type = models.CharField('製法',max_length=100,blank=True,choices = SEIHO)                          #製法
        sake_type = models.CharField('種類',max_length=100,blank=True,choices = SYURUI)     #種類
        dosu = models.IntegerField('度数',blank=True)        #度数
        img_path = models.CharField('画像のパス',max_length=200, blank=True,default='')  #画像パス
        note = models.CharField('備考',max_length=500, blank=True,default='')           #備考
        karasa = models.CharField('辛さ',max_length=100,blank=True,default=0,choices = KARASA)
        upduser = models.CharField('更新者',max_length=150, blank=True,default='')
        updtime = models.DateTimeField('更新日時',blank=True,default=timezone.now)

        def __str__(self):
            return self.name

class otumami(models.Model):

    name = models.CharField('おつまみ名',max_length=128, blank=True)
    upduser = models.CharField('更新者',max_length=150, blank=True,default='')
    updtime = models.DateTimeField('更新日時',blank=True,default=timezone.now)

    def __str__(self):
        return self.name

class otumami_detail(models.Model):

    name = models.CharField('おつまみ名',max_length=128, blank=True,default='')
    otumami_id = models.ForeignKey('otumami',db_column='otumami_id',on_delete=models.CASCADE)
    upduser = models.CharField('更新者',max_length=150, blank=True,default='')
    updtime = models.DateTimeField('更新日時',blank=True,default=timezone.now)

    def __str__(self):
        return self.name

class otumami_with_sake(models.Model):

    sake_id = models.ForeignKey('sake',db_column='sake_id',on_delete=models.CASCADE,default='')
    otumami_id = models.ForeignKey('otumami',db_column='otumami_id',on_delete=models.CASCADE,default='')
    upduser = models.CharField('更新者',max_length=150, blank=True,default='')
    updtime = models.DateTimeField('更新日時',blank=True,default=timezone.now)

    def __str__(self):
        return self.name

class tag(models.Model):

    tag_name = models.CharField('タグ名',max_length=100,blank= True,default='')
    upduser = models.CharField('更新者',max_length=150, blank=True,default='')
    updtime = models.DateTimeField('更新日時',blank=True,default=timezone.now)

    def __str__(self):
        return self.name

class tag_relation(models.Model):

    tag_id = models.ForeignKey('tag',db_column='tag_id', on_delete=models.CASCADE)
    sake_id =models.ForeignKey('sake',db_column='sake_id', on_delete=models.CASCADE)
    otumami_id =models.ForeignKey('otumami',db_column='otumami_id', on_delete=models.CASCADE)
    upduser = models.CharField('更新者',max_length=150, blank=True,default='')
    updtime = models.DateTimeField('更新日時',blank=True,default=timezone.now)

    def __str__(self):
        return self.name

class advas(models.Model):

   name = models.CharField('ユーザー名',max_length=128, blank=True,default='')
   sake_id =models.ForeignKey('sake',db_column='sake_id', on_delete=models.CASCADE)
   otumami_id =models.ForeignKey('otumami',db_column='otumami_id', on_delete=models.CASCADE)
   adv_info = models.CharField('広告情報',max_length=100, blank=True,default='')
   adv_type = models.IntegerField('広告区分',blank=True)
   upduser = models.CharField('更新者',max_length=150, blank=True,default='')
   updtime = models.DateTimeField('更新日時',blank=True,default=timezone.now)

   def __str__(self):
       return self.name

class like(models.Model):

   name = models.CharField('ユーザー名',max_length=128, blank=True,default='')
   sake_id =models.ForeignKey('sake',db_column='sake_id', on_delete=models.CASCADE)
   otumami_id =models.ForeignKey('otumami',db_column='otumami_id', on_delete=models.CASCADE)
   adv_info = models.CharField('広告情報',max_length=100, blank=True,default='')
   adv_type = models.IntegerField('広告区分',blank=True)
   upduser = models.CharField('更新者',max_length=150, blank=True,default='')
   updtime = models.DateTimeField('更新日時',blank=True,default=timezone.now)

   def __str__(self):
       return self.name

class event(models.Model):

   event_name = models.CharField('イベント名',max_length=100, blank=True,default='')
   event_info = models.CharField('広告情報',max_length=300, blank=True,default='')
   upduser = models.CharField('更新者',max_length=150, blank=True,default='')
   updtime = models.DateTimeField('更新日時',blank=True,default=timezone.now)

   def __str__(self):
       return self.name

class event_manage(models.Model):

   event_id =models.ForeignKey('event',db_column='event_id', on_delete=models.CASCADE)
   upduser = models.CharField('更新者',max_length=150, blank=True,default='')
   updtime = models.DateTimeField('更新日時',blank=True,default=timezone.now)

   def __str__(self):
       return self.name
