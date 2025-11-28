from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, List

# Main app
app = FastAPI()
# Router for the api
router = APIRouter()

class Account(BaseModel):
    account_id: str
    user_name: str
    email: str
    password: str  # In a real app, this should be hashed
    balance: float

class SignUpRequest(BaseModel):
    username: str
    email: str
    password: str

class SignInRequest(BaseModel):
    username: str
    password: str

class DepositRequest(BaseModel):
    amount: float

class TransferRequest(BaseModel):
    from_account_id: str
    to_account_id: str
    amount: float

# In-memory database
db: Dict[str, Account] = {}

@router.get("/signup", response_model=Account)
def signup(request: SignUpRequest):
    account_id = request.username
    print("Signup request received for:", account_id)
    if account_id in db:
        raise HTTPException(status_code=400, detail="Username already exists")
    account = Account(
        account_id=account_id,
        user_name=request.username,
        email=request.email,
        password=request.password,
        balance=0.0
    )
    db[account_id] = account
    return account

@router.get("/signin")
def signin(request: SignInRequest):
    account = db.get(request.username)
    if not account or account.password != request.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"message": f"Sign-in successful! Welcome, {account.user_name}."}


@router.get("/")
def read_root():
    return {"message": "Welcome to the Bank API 778"}

@router.get("/accounts/{account_id}", response_model=Account)
def get_account(account_id: str):
    if account_id not in db:
        raise HTTPException(status_code=404, detail="Account not found")
    return db[account_id]

@router.get("/accounts", response_model=List[Account])
def list_accounts():
    return list(db.values())

@router.post("/accounts/{account_id}/deposit", response_model=Account)
def deposit(account_id: str, request: DepositRequest):
    if account_id not in db:
        raise HTTPException(status_code=404, detail="Account not found")
    if request.amount <= 0:
        raise HTTPException(status_code=400, detail="Deposit amount must be positive")
    db[account_id].balance += request.amount
    return db[account_id]

@router.post("/transfer")
def transfer(request: TransferRequest):
    if request.from_account_id not in db:
        raise HTTPException(status_code=404, detail="Sender account not found")
    if request.to_account_id not in db:
        raise HTTPException(status_code=404, detail="Receiver account not found")
    if request.amount <= 0:
        raise HTTPException(status_code=400, detail="Transfer amount must be positive")
    if db[request.from_account_id].balance < request.amount:
        raise HTTPException(status_code=400, detail="Insufficient funds")
    
    db[request.from_account_id].balance -= request.amount
    db[request.to_account_id].balance += request.amount
    
    return {"message": "Transfer successful"}

@router.delete("/accounts/{account_id}")
def delete_account(account_id: str):
    if account_id not in db:
        raise HTTPException(status_code=404, detail="Account not found")
    del db[account_id]
    return {"detail": "Account deleted successfully"}

app.include_router(router, prefix="/api")

# Need to also fix the frontend javascript to point to the new /api endpoints