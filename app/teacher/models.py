from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Teacher:
    id: int
    name: str
    education: Optional[str] = field(default='Bachelor')
    created_at: Optional[datetime] = field(default=datetime.now)