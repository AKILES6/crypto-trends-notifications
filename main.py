from services.coingecko_service import CoinGecko
from services.email_service import EmailService
from utils.load_env import *
from services.email_formatter import EmailFormatter
import time
from datetime import datetime


cg = CoinGecko()
email_service = EmailService(sender_email, gmail_app_pass)


def main():
    onchain_categories = cg.get_onchain_categories()
    top_onchain_categories = onchain_categories[0:4]

    searches = cg.get_trending_searches()
    top_coin_searches = searches.coins[0:4]
    top_nft_searches = searches.nfts[0:4]
    top_coin_categories = searches.categories[0:4]

    top_coin_searches_html = EmailFormatter.generate_html(
        "Top Coin Searches on CoinGecko",
        top_coin_searches,
        "item.name",
        field_paths={
            "Market Cap Rank": "item.market_cap_rank",
            "Price in BTC": "item.price_btc",
        },
    )

    top_nft_searches_html = EmailFormatter.generate_html(
        "Top NFT Searches on CoinGecko",
        top_nft_searches,
        "name",
        field_paths={
            "Floor Price": "data.floor_price",
            "24h Price Change %": "data.floor_price_in_usd_24h_percentage_change",
        },
    )

    top_category_searches_html = EmailFormatter.generate_html(
        "Top Coin Category Searches on CoinGecko",
        top_coin_categories,
        "name",
        field_paths={
            "1h Mcap Change %": "market_cap_1h_change",
            "Number of Coins": "coin_count",
        },
    )

    top_onchain_categories_html = EmailFormatter.generate_html(
        "Top DEX Coin Categories by Volume",
        top_onchain_categories,
        "attributes.name",
        field_paths={
            "Description": "attributes.description",
            "1h Volume Change %": "attributes.volume_change_percentage.h1",
        },
    )

    content = "".join(
        [
            top_coin_searches_html,
            top_nft_searches_html,
            top_category_searches_html,
            top_onchain_categories_html,
        ]
    )

    email_service.send_email(
        recipient_email=sender_email,
        subject=f"Crypto Trend Updates {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        body=content,
    )


if __name__ == "__main__":
    while True:
        main()
        print("Cycle complete, waiting...")
        time.sleep(86400)  # Sleep for 24h in seconds.
