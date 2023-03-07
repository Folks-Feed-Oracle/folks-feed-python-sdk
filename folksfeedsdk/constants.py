from enum import EnumMeta


ALGO_PARAMS = {"unit-name": "ALGO", "decimals": 6}


class OracleAppId(EnumMeta):
    TESTNET = 159512493
    MAINNET = 1040271396


class MainnetAssetId(EnumMeta):
    ALGO = 0
    gALGO = 793124631
    gALGO3 = 694432641
    USDC = 31566704
    USDt = 312769
    goBTC = 386192725
    goETH = 386195940
    Planets = 27165954
    OPUL = 287867876
    GARD = 684649988
    goUSD = 672913181


class TestnetAssetId(EnumMeta):
    ALGO = 0
    USDC = 67395862
    USDt = 67396430
    goBTC = 67396528
    goETH = 76598897
    Planets = 408947
    OPUL = 159508817
    GARD = 161324440
    goUSD = 161324536
