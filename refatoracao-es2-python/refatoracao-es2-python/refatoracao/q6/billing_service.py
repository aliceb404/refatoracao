from enum import Enum


class Plan(Enum):
    FREE = "FREE"
    STUDENT = "STUDENT"
    PRO = "PRO"
    ENTERPRISE = "ENTERPRISE"


class BillingService:

    def monthly_price(self, plan: Plan, active_users: int, priority_support: bool) -> float:
        if plan == Plan.FREE:
            price = 0.0
        elif plan == Plan.STUDENT:
            price = 19.90
        elif plan == Plan.PRO:
            price = 49.90 + (active_users * 1.25)
        elif plan == Plan.ENTERPRISE:
            price = 199.90 + (active_users * 0.90)
        else:
            raise ValueError()

        if priority_support and plan != Plan.FREE:
            price += 59.90
        if active_users > 200 and plan == Plan.PRO:
            price *= 0.95
        return round(price, 2)
