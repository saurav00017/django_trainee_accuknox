Yes, Django signals run in the same thread as the caller by default.

# Proof with Code Snippet
import threading
from django.dispatch import Signal, receiver

# Create a signal
my_signal = Signal()

# Define a receiver function
@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print(f"Receiver is running in thread: {threading.get_ident()}")

# Send the signal
print(f"Caller is running in thread: {threading.get_ident()}")
print("Sending signal...")
my_signal.send(sender=None)
print("Signal sent.")