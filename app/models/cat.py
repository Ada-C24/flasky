from ..db import db
from sqlalchemy.orm import Mapped, mapped_column

class Cat(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    color: Mapped[str]
    personality: Mapped[str]
    
    def to_dict(self):
        return {
            "id": self.id, 
            "name": self.name, 
            "color": self.color,
            "personality": self.personality
        }