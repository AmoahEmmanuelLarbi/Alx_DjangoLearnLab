from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.conf import settings


@receiver(post_migrate)
def create_role(sender, **kwargs):
    if sender.name != "books":
        return

    # create groups
    admins, admins_created = Group.objects.get_or_create(name="Admins")
    editors, editors_created = Group.objects.get_or_create(name="Admins")
    viewers, viewers_created = Group.objects.get_or_create(name="Viewers")

    # get Book permissions
    permissions = Permission.objects.filter(
        content_type__app_label="books", content_type__model="book"
    )

    # Admins: all permissions
    admins.permissions.set(permissions)

    # Editors: add, change,  view
    editors.permissions.set(
        permissions.filter(
            codename__in=[
                "can_add",
                "can_change",
            ]
        )
    )

    # Viewers: view only
    viewers.permissions.set(permissions.filter(codename="can_view"))


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def assign_user_to_group(sender, instance, created, **kwargs):
#     if created:
#         group = Group.objects.filter(
#             name__iexact=instance.role.capitalize() + "s"
#         ).first()

#         if group:
#             instance.groups.add(group)
