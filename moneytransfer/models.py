from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Agent(models.Model):
    """
    Model to represent the agent locations or IDs that facilitate the money transfer.
    """
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} - {self.location}"


class Sender(models.Model):
    """
    Model to represent the sender of the money transfer.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    government_issued_id = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.username} - {self.nationality}"


class Receiver(models.Model):
    """
    Model to represent the receiver of the money transfer.
    """
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    government_issued_id = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.full_name


class Transaction(models.Model):
    """
    Model to represent a money transfer transaction.
    """
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
        ('Failed', 'Failed'),
    ]

    sender = models.ForeignKey(Sender, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Receiver, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    purpose = models.TextField()
    mtcn = models.CharField(max_length=15, unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Transaction {self.mtcn} - {self.sender.user.username} to {self.receiver.full_name}"
