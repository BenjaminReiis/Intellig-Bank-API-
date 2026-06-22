from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from app.database import get_db
from app.models.account import Account
from app.models.user import User
from app.core.dependencies import get_current_user

router = APIRouter(
    prefix="/accounts",
    tags=["Accounts"]
)


@router.post("/create")
def create_account(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    account = db.query(Account).filter(
        Account.owner_id == current_user.id
    ).first()

    if account:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already has an account."
        )

    new_account = Account(
        owner_id=current_user.id,
        balance=0.0
    )

    db.add(new_account)
    db.commit()
    db.refresh(new_account)

    return {
        "message": "Account created successfully.",
        "account_id": new_account.id,
        "balance": new_account.balance
    }


@router.get("/me")
def get_my_account(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    account = db.query(Account).filter(
        Account.owner_id == current_user.id
    ).first()

    if not account:
        raise HTTPException(
            status_code=404,
            detail="Account not found."
        )

    return account
