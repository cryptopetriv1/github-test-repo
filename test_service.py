import asyncio
import httpx
from app.services.dexscreener_service import DexScreenerService

async def test_service():
    service = DexScreenerService()
    # Testing with WETH address on Ethereum
    token_address = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
    print(f"Testing with address: {token_address}")
    data = await service.get_token_data(token_address)
    
    if data:
        print("Successfully fetched data:")
        print(data.model_dump_json(indent=2))
    else:
        print("Failed to fetch data.")

if __name__ == "__main__":
    asyncio.run(test_service())
