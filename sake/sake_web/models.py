from django.contrib import auth
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.

class sake(models.Model):

    #(#'~~'#)選択肢作成よろしく
    #============================================
    TODOHUKEN = ((1, '大阪'), (2, '京都'))
    SEIHO = ((1, '生'), (2, '火入れ'))
    SYURUI =  ((1, '大吟醸'), (2, '吟醸'),(3,'純米吟醸'))
    KARASA =  ((1, '辛さ１'), (2, '辛さ２'))
    #=============================================

    name = models.CharField('銘柄',max_length=100,default='')                       #銘柄
    creater = models.CharField('蔵元',max_length=100, blank=True,default='')        #蔵元
    region = models.IntegerField('都道府県',blank=True,choices = TODOHUKEN)                             #地域 0:北海道 1:東北　2:関東 3:北陸　4:近畿 5:中国　6:四国 7九州
    created_type = models.IntegerField('製法',blank=True,choices = SEIHO)                          #製法
    sake_type = models.IntegerField('種類',blank=True,choices = SYURUI)     #種類
    dosu = models.IntegerField('度数',blank=True)        #度数
    img_path = models.CharField('画像のパス',max_length=200, blank=True,default='')  #画像パス
    note = models.CharField('備考',max_length=500, blank=True,default='')           #備考
    karasa = models.IntegerField('辛さ',blank=True,default=0,choices = KARASA)
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
   user_id =models.ForeignKey('user',db_column='user_id', on_delete=models.CASCADE)
   upduser = models.CharField('更新者',max_length=150, blank=True,default='')
   updtime = models.DateTimeField('更新日時',blank=True,default=timezone.now)

   def __str__(self):
       return self.name


class UserManager(BaseUserManager):
    '''ユーザーマネージャー.'''

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        '''メールアドレスでの登録を必須にする'''
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        '''is_staff(管理サイトにログインできるか)と、is_superuer(全ての権限)をFalseに'''
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        '''スーパーユーザーは、is_staffとis_superuserをTrueに'''
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class AbstractUser(AbstractBaseUser, PermissionsMixin):
    '''
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
    Username and password are required. Other fields are optional.
    '''

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={
            'unique': _('A user with that username already exists.'),
        },blank=True
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        '''
        Return the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''Return the short name for the user.'''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''Send an email to this user.'''
        send_mail(subject, message, from_email, [self.email], **kwargs)

class User(AbstractUser):
    '''
    Users within the Django authentication system are represented by this
    model.
    Username and password are required. Other fields are optional.
    '''
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
