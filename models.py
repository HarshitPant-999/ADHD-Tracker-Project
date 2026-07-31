from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey
from datetime import datetime

DateTime = datetime.now()
print(DateTime)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)


class Entry(db.Model):
    __tablename__ = "entry"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    timestamp: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    trigger: Mapped[str] = mapped_column(Text, nullable=False)
    reset_info: Mapped[str] = mapped_column(Text, nullable=False)
