from pydantic import BaseModel, ConfigDict, Field


class Deposit(BaseModel):
    amount: float = Field(gt=0)


class Withdraw(BaseModel):
    amount: float = Field(gt=0)


class TransactionResponse(BaseModel):
    id: int
    type: str
    amount: float

    model_config = ConfigDict(from_attributes=True)
