from algosdk.v2client.algod import AlgodClient
from folksfeedsdk.folks_feed_client import FolksFeedClient
from folksfeedsdk.constants import ORACLE_TESTNET_ID, TestnetAssetId
from folksfeedsdk.models.asset_info import AssetInfo

algod_address = "https://node.testnet.algoexplorerapi.io"
algod_token = ""
algod_client = AlgodClient(algod_token, algod_address)


ffo_client = FolksFeedClient(algod_client, ORACLE_TESTNET_ID)

algo_info: AssetInfo = ffo_client.get_asset_info(TestnetAssetId.ALGO)
print(algo_info.__dict__)

goETH_info: AssetInfo = ffo_client.get_asset_info(TestnetAssetId.goETH)
print(goETH_info.__dict__)

goBTC_price = ffo_client.get_asset_price(TestnetAssetId.goBTC)
print(goBTC_price)
