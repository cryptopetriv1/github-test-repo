from fastapi import APIRouter, HTTPException
from app.services.dexscreener_service import DexScreenerService
from app.schemas.token_schema import TokenomicsResponse

router = APIRouter()
dex_service = DexScreenerService()

@router.get("/token/{token_address}", response_model=TokenomicsResponse)
async def get_token_tokenomics(token_address: str):
    data = await dex_service.get_token_data(token_address)
    
    if not data:
        return TokenomicsResponse(
            success=False,
            error="Token data not found or error fetching data."
        )
    
    return TokenomicsResponse(
        success=True,
        data=data
    )
