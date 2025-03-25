"""Избегание повторения декораторов или декорирование всех подклассов"""

import datetime
from decimal import Decimal
from uuid import UUID

import attr


class EventMeta(type):
    def __new__(cls, name, bases, namespace):
        new_cls = super().__new__(cls, name, bases, namespace)
        return attr.s(frozen=True, auto_attribs=True)(new_cls)  # (!)


class Event(metaclass=EventMeta):
    created_at: datetime


class InvoiceIssued(Event):
    invoice_uuid: UUID
    customer_uuid: UUID
    total_amount: Decimal
    total_amount_currency: str
    due_date: datetime


class InvoiceOverdue(Event):
    invoice_uuid: UUID
    customer_uuid: UUID
