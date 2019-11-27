from django.contrib import admin
from .models import Player, Location, Item, ItemType, Messages
# Register your models here.
admin.site.register(Player)
admin.site.register(Location)
admin.site.register(Item)
admin.site.register(ItemType)
admin.site.register(Messages)

