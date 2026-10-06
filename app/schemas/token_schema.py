from pydantic import BaseModel
from typing import Optional, Dict, Any

class TokenomicsData(BaseModel):
    symbol: str
    name: str
    address: str
    price_usd: float
    market_cap: Optional[float] = None
    fdv: Optional[float] = None
    volume_24h: Optional[float] = None
    liquidity_usd: Optional[float] = None
    image_url: Optional[str] = None
    holders: Optional[int] = None  # Placeholder for now
    dex_url: Optional[str] = None

class TokenomicsResponse(BaseModel):
    success: bool
    data: Optional[TokenomicsData] = None
    error: Optional[str] = None
