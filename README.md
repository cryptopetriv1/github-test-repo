# DexTokenomics API (Solana)

This is a FastAPI backend designed to provide structured tokenomics data for LLMs (like Claude), specialized for the **Solana** ecosystem. It aggregates data from DexScreener.

## Features
- Fetches price, market cap, FDV, 24h volume, and liquidity.
- **Restricted to Solana tokens only.**
- Returns structured JSON optimized for LLM consumption.
- Async implementation using `httpx`.

## Installation

1. Navigate to the project directory:
   ```bash
   cd D:\Crypto\VC\dex-tokenomics-api
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the API

Start the server with Uvicorn:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

## API Endpoints

### Get Tokenomics Data
`GET /api/v1/token/{token_address}`

**Example Request:**
`GET http://localhost:8000/api/v1/token/EPjFW3F24v1666uY7S91B7T5A9pBvY8R3K9vC6T7v7v7` (Note: Use a valid Solana token address)

**Example Response:**
```json
{
  "success": true,
  "data": {
    "symbol": "USDC",
    "name": "USDC",
    "address": "EPjFW3F24v1666uY7S91B7T5A9pBvY8R3K9vC6T7v7v7",
    "price_usd": 1.0,
    "market_cap": 30000000000.0,
    "fdv": 30000000000.0,
    "volume_24h": 500000000.0,
    "liquidity_usd": 1000000000.0,
    "image_url": "https://...",
    "holders": null,
    "dex_url": "https://..."
  },
  "error": null
}
```
