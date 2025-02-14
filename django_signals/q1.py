
# By default, Django signals are executed synchronously.

# Proof with Code Snippet
from django.dispatch import Signal, receiver

# Create a signal
my_signal = Signal()

# Define a receiver function
@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print("Receiver is running...")
    # Simulate some work
    for i in range(3):
        print(f"Working... {i}")
    print("Receiver finished.")

# Send the signal
print("Sending signal...")
my_signal.send(sender=None)
print("Signal sent.")