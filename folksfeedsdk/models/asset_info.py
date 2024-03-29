from folksfeedsdk.utils import gs_to_int
from dataclasses import dataclass


@dataclass
class AssetInfo:
    asset_name: str
    price_threshold: int
    raw_price: int
    price: int
    latest_timestamp: int

    @classmethod
    def from_global_state(cls, name, decimals, gs):
        asset_name = name
        price_threshold = round(gs_to_int(gs, 16, 4) / 1e4, 2)
        raw_price = gs_to_int(gs, 0, 8)
        price = raw_price * (10**decimals / 1e14)
        latest_timestamp = gs_to_int(gs, 8, 8)
        return cls(asset_name, price_threshold, raw_price, price, latest_timestamp)
