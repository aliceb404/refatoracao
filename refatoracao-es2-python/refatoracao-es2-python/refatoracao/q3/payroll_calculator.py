from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Overtime:
    hours: int
    hour_rate: float


@dataclass(frozen=True)
class Employee:
    base_salary: float
    overtimes: list[Overtime]
    has_meal_voucher: bool
    health_plan_deduction: float


class PayrollCalculator:

    def monthly_net_salary(self, e: Employee) -> float:
        base = e.base_salary
        overtime = 0.0
        for ot in e.overtimes:
            overtime += ot.hours * ot.hour_rate

        gross = base + overtime
        if gross <= 3000:
            tax = gross * 0.08
        elif gross <= 7000:
            tax = gross * 0.12
        else:
            tax = gross * 0.18

        meal_voucher = 450.0 if e.has_meal_voucher else 0.0
        health_plan = e.health_plan_deduction

        net = gross - tax - health_plan + meal_voucher
        return round(net, 2)
