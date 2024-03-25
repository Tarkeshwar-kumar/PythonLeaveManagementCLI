from dataclasses import dataclass
from typing import Optional
from data import Credentals

@dataclass
class LeaveStats:
    leaves_total: int
    leaves_taken: int
    leave_applied: int

@dataclass
class Employee:
    first_name: str
    middle_name: Optional[list[str]]
    last_name: str
    email: str
    

