from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    type: Mapped[str] = mapped_column(
        String(20)
    )

    amount: Mapped[float] = mapped_column(
        Float
    )

    account_id: Mapped[int] = mapped_column(
        ForeignKey("accounts.id")
    )

    account = relationship(
        "Account",
        back_populates="transactions"
    )
