from sqlalchemy import Float
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database import Base


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    balance: Mapped[float] = mapped_column(
        Float,
        default=0.0
    )

    owner_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True
    )

    owner = relationship(
        "User",
        back_populates="account"
    )

    transactions = relationship(
        "Transaction",
        back_populates="account",
        cascade="all, delete-orphan"
    )
