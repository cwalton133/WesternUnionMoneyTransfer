from django.contrib import admin
from .models import Agent, Sender, Receiver, Transaction


# Register your models here.

admin.site.register(Agent)
admin.site.register(Sender)
admin.site.register(Receiver)
admin.site.register(Transaction)
