from algosdk.v2client.algod import AlgodClient
from folksfeedsdk.folks_feed_client import FolksFeedClient
from folksfeedsdk.constants import OracleAppId, TestnetAssetId, MainnetAssetId
from folksfeedsdk.models.asset_info import AssetInfo

network = "mainnet"

if network == "mainnet":
    algod_address = "https://node.algoexplorerapi.io"
    oracle_app_id = OracleAppId.MAINNET
    asset_id = MainnetAssetId
else:
    algod_address = "https://node.testnet.algoexplorerapi.io"
    oracle_app_id = OracleAppId.TESTNET
    asset_id = TestnetAssetId


algod_client = AlgodClient("", algod_address)


ffo_client = FolksFeedClient(algod_client, oracle_app_id)

algo_info: AssetInfo = ffo_client.get_asset_info(asset_id.ALGO)
print(algo_info.__dict__)

goETH_info: AssetInfo = ffo_client.get_asset_info(asset_id.OPUL)
print(goETH_info.__dict__)

goBTC_price = ffo_client.get_asset_price(asset_id.goBTC)
print(goBTC_price)
