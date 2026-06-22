from pydantic import BaseModel, ConfigDict


class AccountResponse(BaseModel):
    id: int
    balance: float
    owner_id: int

    model_config = ConfigDict(from_attributes=True)
