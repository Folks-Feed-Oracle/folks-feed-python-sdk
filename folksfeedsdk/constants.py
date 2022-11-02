from enum import EnumMeta

ORACLE_TESTNET_ID = 120211944

ALGO_PARAMS = {"unit-name": "ALGO", "decimals": 6}


class MainnetAssetId(EnumMeta):
    ALGO = 0
    gALGO = 793124631
    USDC = 31566704
    USDt = 312769
    goBTC = 386192725
    goETH = 386195940
    Planet = 27165954


class TestnetAssetId(EnumMeta):
    ALGO = 0
    USDC = 67395862
    USDt = 67396430
    goBTC = 67396528
    goETH = 76598897
    Planet = 408947
