from __future__ import annotations

from typing import List, TYPE_CHECKING
from .person import Person
from datetime import date

if TYPE_CHECKING:
    from .loan import Loan

class Reader(Person):
    MAX_LOANS = 3

    def __init__(self, id: int, name: str, birthdate: date, contact_info: str):
        super().__init__(id, name, birthdate, contact_info)
        self._fine_amount = 0.0
        self._active_loans: List[Loan] = []

    @property
    def active_loans(self) -> List[Loan]:
        return self._active_loans
    
    @property
    def fine_amount(self) -> float:
        return self._fine_amount
    
    def can_loan(self) -> bool:
        return len(self._active_loans) < Reader.MAX_LOANS

    def add_loan(self, loan: Loan):
        if self.can_loan():
            self._active_loans.append(loan)
        else:
            raise ValueError(f"Reader has reached the maximum loan limit of {Reader.MAX_LOANS}.")

    def remove_loan(self, loan: Loan):
        if loan in self._active_loans:
            self._active_loans.remove(loan)
            
    def add_fine(self, value: float):
        if value > 0:
            self._fine_amount += value

    def pay_fine(self, amount_paid: float):
        if amount_paid > 0:
            self._fine_amount -= amount_paid
            if self._fine_amount < 0:
                self._fine_amount = 0.0
    
    def has_pending_fines(self) -> bool:
        return self._fine_amount > 0

    def __str__(self) -> str:
        return f"{super().__str__()}, Active Loans: {len(self._active_loans)}, Fines: ${self._fine_amount:.2f}"