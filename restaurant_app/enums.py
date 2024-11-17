from enum import Enum


class BookingStatus(Enum):
    REQUESTED = "requested"
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELED = "canceled"
    ABANDONED = "abandoned"

class PaymentStatus(Enum):
    PENDING = "Pending"
    COMPLETED = "Completed"
    FAILED = "Failed"
    REFUNDED = "Refunded"
    CANCELED = "Canceled"

