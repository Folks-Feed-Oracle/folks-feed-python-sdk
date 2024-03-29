# Folks Feed Oracle Python SDK

The official Python SDK for the Folks Feed Oracle

(*This SDK is to be considered a beta version.*)
### Overview

This SDK allows you to read the oracle prices saved in the Algorand Smart Contract:
 - Testnet app id: [159512493](https://testnet.algoexplorer.io/application/159512493). 
 - Mainnet app id: [1040271396](https://algoexplorer.io/application/1040271396). 

It currently supports these price feeds:
- USDC
- USDt
- ALGO
- goETH
- goBTC
- Planets
- OPUL
- gALGO
- gALGO3
- GARD
- goUSD

Prices are updated every 10 seconds.

### Running examples

```bash
# install reqs
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
# run example
python3 -m examples.get_prices
```

### PyTEAL 
To integrate Folks Feed Oracle in your ASC1:
```python
@Subroutine(TealType.uint64)
def get_asset_price(folks_feed_oracle: abi.Application, asa_id: abi.Asset):
    asa_info = App.globalGetEx(folks_feed_oracle.application_id(), Itob(asa_id.asset_id()))
    return Seq(asa_info, Assert(asa_info.hasValue()), ExtractUint64(asa_info.value(), Int(0)))
```