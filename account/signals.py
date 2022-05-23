from account.models import CustomerID, User
from django.db.models.signals import post_save
from django.dispatch import receiver

import shortuuid


@receiver(post_save, sender=User)
def create_customer_id(sender, instance, created, **kwargs):
    if created:
        user = instance
        print(f"{user=}")

        s = shortuuid.ShortUUID(alphabet="0123456789")
        otp = s.random(length=6)
        
        print(f"{user.user_type.id=}")

        if user.user_type.id == 1:
            customer_id = CustomerID.objects.create(
                user = instance,
                customer_id = otp
            ).save()

            print(f"{customer_id=}")