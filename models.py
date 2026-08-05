from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey, DateTime
from datetime import datetime

#DateTime = datetime.now()
#print(DateTime)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)


class Entry(db.Model):
    __tablename__ = "entry"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    timestamp: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    trigger: Mapped[str] = mapped_column(Text, nullable=False)
    reset_info: Mapped[str] = mapped_column(Text, nullable=True)
    reset_time : Mapped[int] = mapped_column(Integer, nullable=True)
    @property
    def time_block(self):
        hour = self.timestamp.hour
        if hour < 10:
            return "Morning"
        elif hour < 15:
            return "Afternoon"
        elif hour < 19:
            return "Evening"
        else:
            return "Night"

