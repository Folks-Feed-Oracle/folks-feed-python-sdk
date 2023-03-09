from algosdk.v2client.indexer import IndexerClient
from algosdk.v2client.algod import AlgodClient
from folksfeedsdk.constants import ALGO_PARAMS
from folksfeedsdk.utils import gs_to_int
from folksfeedsdk.models.asset_info import AssetInfo


class FolksFeedClient:
    def __init__(self, algod_client: AlgodClient, indexer_client: IndexerClient, app_id: int):
        self.algod_client = algod_client
        self.indexer_client = indexer_client
        self.app_id = app_id

    def get_global_states(self, round_num):
        return (
            self.algod_client.application_info(self.app_id)["params"]["global-state"]
            if not round_num
            else self.indexer_client.search_transactions(
                limit=1,
                sig_type="sig",
                min_round=round_num - 20,
                max_round=round_num,
                application_id=self.app_id,
            )["transactions"][0]["global-state-delta"]
        )

    def get_asset_info(self, asset_id: int, round_num: int = None):
        asset_info_params = self.algod_client.asset_info(asset_id)["params"] if asset_id else ALGO_PARAMS
        name, decimals = asset_info_params["unit-name"], asset_info_params["decimals"]
        global_states = self.get_global_states(round_num)
        for global_state in global_states:
            try:
                if gs_to_int(global_state["key"], 0) == asset_id:
                    gs = global_state["value"]["bytes"]
                    return AssetInfo.from_global_state(name, decimals, gs)
            except:
                continue
        raise Exception("{} ({}) feed not found.".format(asset_id, name))

    def get_asset_price(self, asset_id: int):
        return self.get_asset_info(asset_id).price
