from enum import Enum

class AccountType(Enum):
    MEMBER = "member"
    GUEST = "guest"
    MANAGER = "manager"
    RECEPTIONIST = "receptionist"

class AccountStatus(Enum):
    ACTIVE = "active"
    CLOSED = "closed"
    CANCELED = "canceled"
    BLACKLISTED = 'blacklisted'
