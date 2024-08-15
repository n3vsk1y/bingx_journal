from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title='Bing Journal'
)


users = [
    {'id': 1, 'role': 'admin', 'name': 'Bob'},
    {'id': 2, 'role': 'user', 'name': 'Garry'},
    {'id': 3, 'role': 'moderator', 'name': 'Bill'},
]

trades = [
    {'id': 1, 'user_id': 1, 'ticker': 'BTCUSDT', 'side': 'LONG', 'price': 60000, 'amount': 1}
]


class User(BaseModel):
    id: int
    role: str
    name: str


@app.get('/users/{user_id}', response_model=List[User])
async def get_user(user_id: int):
    return [user for user in users if user.get('id') == user_id]


class Trade(BaseModel):
    id: int
    user_id: int
    ticker: str = Field(max_length=20)
    side: str
    price: float = Field(ge=0)
    amount: float


@app.post('/trades')
async def add_trade(new_trades: List[Trade]):
    trades.extend(new_trades)
    return {'status': 200, 'data': trades}


