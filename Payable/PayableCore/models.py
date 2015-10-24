import re

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,\
    PermissionsMixin
from django.utils import timezone
from django.core import validators
from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext_lazy as _



class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, is_staff, is_superuser, first_name, last_name, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(_('The given username must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                 is_staff=is_staff, is_active=True,
                 is_superuser=is_superuser,
                 last_login=now,
                 first_name=first_name,
                 last_name=last_name,
                 **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    def create_superuser(self, username, email, password, first_name, last_name):
        user=self._create_user(username, email, password, True, True, first_name, last_name)
        user.is_active=True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, verbose_name='Username', unique=True, max_length=255,
                                help_text=_('Required. 255 characters or fewer. Letters, numbers and @/./+/-/_ characters'),
                                validators=[
                                  validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid username.'), _('invalid'))
                                ])
    email = models.EmailField(db_index=True, verbose_name='Email', unique=True, max_length=255, blank=True)
    first_name = models.CharField(verbose_name='First_Name', max_length=20)
    last_name = models.CharField(verbose_name='Last_Name', max_length=20)
    timezone = models.CharField(verbose_name='Timezone Information', blank=True, null=True, max_length=250)
    is_active = models.BooleanField(verbose_name='Active User', default=False)
    is_staff = models.BooleanField(verbose_name='Staff User', default=False)
    created_at = models.DateTimeField(verbose_name='Created_At', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Updated_At', auto_now=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
    objects = UserManager()
    
    def __unicode__(self):
        return smart_unicode(self.username)
    
    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.rstrip()
    
    def get_short_name(self):
        return self.first_name
        
    def get_primary_email(self):
        return getattr(self, 'email')
