By default, Django signals do not automatically run in the same database transaction as the caller. 

# Proof with Code Snippet
from django.db import transaction, models
from django.dispatch import Signal, receiver
from django.db.models.signals import post_save

# Create a simple model
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Create a signal
my_signal = Signal()

# Define a receiver function for the signal
@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print("Signal received! Creating a MyModel instance...")
    MyModel.objects.create(name="Signal Instance")

# Simulate a transaction
try:
    with transaction.atomic():
        print("Starting transaction...")
        # Send the signal inside the transaction
        my_signal.send(sender=None)
        # Simulate a failure to force a rollback
        raise Exception("Simulated failure to force rollback")
except Exception as e:
    print(f"Transaction rolled back due to: {e}")

# Check if the MyModel instance created by the signal exists
if MyModel.objects.filter(name="Signal Instance").exists():
    print("MyModel instance created by the signal still exists!")
else:
    print("MyModel instance created by the signal was rolled back.")