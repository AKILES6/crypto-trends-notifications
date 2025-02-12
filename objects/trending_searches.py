from dataclasses import dataclass
from typing import List, Optional
from dataclass_wizard import JSONWizard


@dataclass
class CoinItem:
    id: str
    coin_id: int
    name: str
    symbol: str
    market_cap_rank: int
    thumb: str
    small: str
    large: str
    slug: str
    price_btc: float
    score: int


@dataclass
class Coin:
    item: CoinItem


@dataclass
class NFTData:
    floor_price: str
    floor_price_in_usd_24h_percentage_change: str
    h24_volume: str
    h24_average_sale_price: str
    sparkline: str
    content: Optional[str]


@dataclass
class NFT:
    id: str
    name: str
    symbol: str
    thumb: str
    nft_contract_id: int
    native_currency_symbol: str
    floor_price_in_native_currency: float
    floor_price_24h_percentage_change: float
    data: NFTData


@dataclass
class Category:
    id: int
    name: str
    market_cap_1h_change: float
    slug: str
    coins_count: str


@dataclass
class TrendingSearches(JSONWizard):
    coins: List[Coin]
    nfts: List[NFT]
    categories: List[Category]
