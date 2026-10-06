import httpx
from typing import Optional
from app.schemas.token_schema import TokenomicsData

class DexScreenerService:
    BASE_URL = "https://api.dexscreener.com/latest/dex/tokens/"
    TARGET_CHAIN = "solana"

    async def get_token_data(self, token_address: str) -> Optional[TokenomicsData]:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{self.BASE_URL}{token_address}")
                response.raise_for_status()
                data = response.json()

                if not data.get("pairs"):
                    return None

                # Filter pairs to find only those on the Solana chain
                solana_pairs = [
                    pair for pair in data["pairs"] 
                    if pair.get("chainId") == self.TARGET_CHAIN
                ]

                if not solana_pairs:
                    return None

                # Pick the first Solana pair (usually the one with highest liquidity/volume)
                pair = solana_pairs[0]
                base_token = pair.get("baseToken", {})
                
                # Extracting values safely
                return TokenomicsData(
                    symbol=base_token.get("symbol", "Unknown"),
                    name=base_token.get("name", "Unknown"),
                    address=base_token.get("address", token_address),
                    price_usd=float(pair.get("priceUsd", 0)),
                    market_cap=float(pair.get("marketCap")) if pair.get("marketCap") else None,
                    fdv=float(pair.get("fdv")) if pair.get("fdv") else None,
                    volume_24h=float(pair.get("volume", {}).get("h24", 0)) if pair.get("volume") else None,
                    liquidity_usd=float(pair.get("liquidity", {}).get("usd", 0)) if pair.get("liquidity") else None,
                    image_url=pair.get("info", {}).get("imageUrl"),
                    holders=None,  # Holders data not directly available in DexScreener API
                    dex_url=pair.get("url")
                )

            except Exception as e:
                print(f"Error fetching data from DexScreener: {e}")
                return None
