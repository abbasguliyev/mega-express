from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator
from .managers import UserManager
import uuid
import shortuuid
# Create your models here.

class UserType(models.Model):
    type_name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.type_name

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(_('name'), max_length=100)
    surname = models.CharField(_('surname'), max_length=100)
    phone = PhoneNumberField(_('phone number'), null=False, blank=False, unique=True)
    fin = models.CharField(
        _('fin code'),
        max_length=7,
        unique=True
    )
    location = models.CharField(_('user location'), max_length=300, null=False, blank=False)
    id_card_photo = models.ImageField(_('user ID card photo'), upload_to="media/account/%Y/%m/%d/", null=True, blank=True)

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    user_type = models.ForeignKey(UserType, on_delete=models.SET_NULL, null=True, blank=True, related_name="users")

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name', 'surname', 'fin']

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    objects = UserManager()

    def __str__(self):
        return f"{self.name} {self.surname} - {self.phone.as_e164}"

class CustomerID(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customer_uuids")
    customer_id = models.PositiveBigIntegerField(primary_key=True, unique=True, editable=False)

    # def save(self, *args, **kwargs):
    #     s = shortuuid.ShortUUID(alphabet="0123456789")
    #     otp = s.random(length=6)
    #     self.customer_id = otp
    #     super(CustomerID, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.user.name} {self.user.surname} - {str(self.customer_id)}"