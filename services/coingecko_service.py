from typing import List, Literal
import requests
from objects.coin_category import Category
from objects.trending_searches import TrendingSearches
from utils.load_env import *


class CoinGecko:
    def __init__(self):
        self.root = "https://pro-api.coingecko.com/api/v3"
        self.headers = {
            "accept": "application/json",
            "x_cg_pro_api_key": f"{cg_api_key}",
        }

    def get_onchain_categories(
        self,
    ) -> List[Category]:
        request_url = self.root + f"/onchain/categories?sort=h1_volume_percentage_desc"

        response = requests.get(request_url, self.headers).json()["data"]
        return [Category.from_dict(item) for item in response]

    def get_trending_searches(
        self,
    ) -> TrendingSearches:
        request_url = self.root + f"/search/trending"

        result = requests.get(request_url, self.headers).json()

        return TrendingSearches.from_dict(result)
