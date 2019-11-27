from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    KNIGHT = 'KN'
    WIZARD = 'WI'
    THIEF = 'TH'
    PALADIN = 'PL'
    CLASS_CHOICES = (
        (KNIGHT, 'Knight'),
        (WIZARD, 'Wizard'),
        (THIEF, 'Thief'),
        (PALADIN, 'Paladin'),
    )
    playerclass = models.CharField(max_length=2, choices=CLASS_CHOICES, default=KNIGHT)
    email = models.EmailField()
    level = models.IntegerField()
    position = models.ForeignKey('Location', on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Player.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.player.save()

class Location(models.Model):
    locationId = models.CharField(max_length=10, primary_key=True)
    description = models.TextField()
    FOREST = 'FO'
    DESERT = 'DS'
    DUNGEON = 'DU'
    RIVER = 'RI'
    OCEAN = 'OC'
    LOCATION_CHOICES = (
        (FOREST, 'Forest'),
        (DESERT, 'Desert'),
        (DUNGEON, 'Dungeon'),
        (RIVER, 'River'),
        (OCEAN, 'Ocean'),
    )
    locationType = models.CharField(max_length=2, choices=LOCATION_CHOICES, default=FOREST)

    def __str__(self):
        return self.locationId


class Item(models.Model):
    itemType = models.ForeignKey('ItemType', on_delete=models.CASCADE)
    quality = models.IntegerField()
    owner = models.ForeignKey('Player', on_delete=models.CASCADE)




class ItemType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Messages(models.Model):
    messageId = models.AutoField(primary_key=True)
    playerFrom = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='player_from')
    playerTo = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    messageText = models.CharField(max_length=1000)

    def __str__(self):
        return self.messageText