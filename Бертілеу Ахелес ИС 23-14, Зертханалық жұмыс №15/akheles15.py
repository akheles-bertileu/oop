import threading
from datetime import datetime

# -----------------------
# Task 1: Singleton Logger
# -----------------------
class Logger:
    _instance = None
    _lock = threading.Lock()  # for thread safety

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
                    cls._instance.logs = []
        return cls._instance

    def log(self, message):
        timestamped = f"{datetime.now()} - {message}"
        self.logs.append(timestamped)
        return timestamped

# -----------------------
# Task 2: Strategy Pattern for Discounts
# -----------------------
class DiscountStrategy:
    def apply(self, price):
        raise NotImplementedError()

class NoDiscount(DiscountStrategy):
    def apply(self, price):
        return price

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent):
        self.percent = percent

    def apply(self, price):
        return price * (1 - self.percent / 100)

class FixedDiscount(DiscountStrategy):
    def __init__(self, amount):
        self.amount = amount

    def apply(self, price):
        return max(0, price - self.amount)

def calculate_total(price, strategy: DiscountStrategy):
    return strategy.apply(price)

# -----------------------
# Task 3: Factory Pattern for Notifications
# -----------------------
class Notification:
    def send(self, message):
        raise NotImplementedError()

class EmailNotification(Notification):
    def send(self, message):
        print(f"Email sent: {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"SMS sent: {message}")

class PushNotification(Notification):
    def send(self, message):
        print(f"Push Notification sent: {message}")

class NotificationFactory:
    _types = {
        "email": EmailNotification,
        "sms": SMSNotification,
        "push": PushNotification
    }

    @classmethod
    def get(cls, channel: str):
        if channel in cls._types:
            return cls._types[channel]()
        else:
            raise ValueError(f"Unknown channel: {channel}")

# -----------------------
# Task 4: Observer Pattern
# -----------------------
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        raise NotImplementedError()

class ConsoleSubscriber(Observer):
    def update(self, message):
        print(f"ConsoleSubscriber received: {message}")

class FileSubscriber(Observer):
    def update(self, message):
        # Simulating writing to file
        print(f"FileSubscriber received: {message} (would be saved to file)")

# -----------------------
# Task 5: Integrated Event Logging System
# -----------------------
class EventLogger(Subject):
    def __init__(self):
        super().__init__()
        self.logger = Logger()  # Singleton Logger

    def log_event(self, message):
        log_msg = self.logger.log(message)
        self.notify(log_msg)

# -----------------------
# Demonstration (run directly)
# -----------------------

# Task 1: Singleton Test
logger1 = Logger()
logger2 = Logger()
logger1.log("System started")
print("Logger singleton test:", logger1 is logger2)
print(logger2.logs)
print()

# Task 2: Strategy Test
price = 200
no_discount = NoDiscount()
perc_discount = PercentageDiscount(10)
fixed_discount = FixedDiscount(30)

print("Original price:", price)
print("No discount:", calculate_total(price, no_discount))
print("10% discount:", calculate_total(price, perc_discount))
print("Fixed 30 discount:", calculate_total(price, fixed_discount))
print()

# Task 3: Factory Test
factory = NotificationFactory()
factory.get("email").send("Hello via Email!")
factory.get("sms").send("Hello via SMS!")
factory.get("push").send("Hello via Push!")
print()

# Task 4 & 5: Observer + Singleton Integration
event_logger = EventLogger()
console_sub = ConsoleSubscriber()
file_sub = FileSubscriber()

event_logger.attach(console_sub)
event_logger.attach(file_sub)

event_logger.log_event("User logged in")
event_logger.log_event("Error occurred")
