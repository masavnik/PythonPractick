# from openpyxl import load_workbook
# from openpyxl.workbook import Workbook
# import requests
# from bs4 import BeautifulSoup
# import selenium
#
#
# year = 2024
# name = f'Стихи/{year}.xlsx'
#
# workbook = load_workbook(filename=name)
# sheet = workbook.active
#
# for row in range(2, sheet.max_row + 1):
#     cell_value = sheet.cell(row=row, column=2).value[-4:]
#     sheet[f'B{row}'] = cell_value
#
# workbook.save(f'{year}.xlsx')


a = {
  "_id": {
    "chain": "bsc",
    "exchange": "sushi",
    "pair": "0x3d41ced5764340265d58ea4996f909eb05e25fdb",
    "token": "0x0cbd6fadcf8096cc9a43d90b45f65826102e3ece",
    "tokenRef": "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c"
  },
  "token": {
    "symbol": "CDT",
    "name": "CheckDot",
    "creationBlock": 12314062,
    "creationTime": "2021-11-02T20:35:21.000Z",
    "metrics": {
      "fdv": 447736256.5980268,
      "holders": 6738,
      "txCount": 272265,
      "circulatingSupply": 7745635.25,
      "maxSupply": 9897808,
      "totalSupply": 9897807.922470633
    },
    "decimals": 18,
    "totalSupply": "9897808000000000000000000",
    "audit": {
      "codeVerified": true,
      "date": "2024-07-29T18:25:30.653Z",
      "lockTransactions": false,
      "mint": false,
      "proxy": false,
      "status": "OK",
      "unlimitedFees": false,
      "version": 1,
      "is_contract_renounced": false,
      "provider": "GoPlus",
      "dextools": {
        "is_open_source": "yes",
        "is_honeypot": "no",
        "is_mintable": "no",
        "is_proxy": "no",
        "slippage_modifiable": "no",
        "is_blacklisted": "no",
        "sell_tax": {
          "min": 0,
          "max": 0,
          "status": "clear"
        },
        "buy_tax": {
          "min": 0,
          "max": 0,
          "status": "clear"
        },
        "is_contract_renounced": "no",
        "is_potentially_scam": "no",
        "transfer_pausable": "no",
        "summary": {
          "providers": {
            "critical": [],
            "warning": [],
            "regular": [
              "creator_address",
              "creator_balance",
              "creator_percent",
              "lp_holder_count",
              "owner_address",
              "owner_balance",
              "owner_percent",
              "is_potentially_scam"
            ]
          },
          "review": {
            "critical": [],
            "warning": [],
            "regular": []
          }
        },
        "updatedAt": "2024-07-29T17:35:59.588Z"
      }
    },
    "info": {
      "cmc": "checkdot",
      "coingecko": "checkdot",
      "description": "The CheckDot platform is a essential checkpoint for the verification for any cryptocurrency project and more.\r\n\r\nWe have been confronted with the lack of transparency of some projects for many years. CheckDot has the ambition to be the first decentralized platform of opinions in various fields: Projects, companies, forms, code and more. Furthermore, CheckDot makes it possible to create requests for advice or audits involving one or two layers of advisors.",
      "dextools": false,
      "blueCheckmark": "true",
      "email": "mail@checkdot.io",
      "ventures": false,
      "extraInfo": "",
      "nftCollection": ""
    },
    "links": {
      "discord": "https://discord.gg/bmwbC4mDcM",
      "medium": "https://checkdot.medium.com/",
      "telegram": "https://t.me/checkdot",
      "twitter": "https://twitter.com/checkdot_proto",
      "website": "https://checkdot.io/",
      "github": "https://github.com/checkdot",
      "bitbucket": "",
      "facebook": "",
      "instagram": "",
      "linkedin": "",
      "reddit": "https://www.reddit.com",
      "tiktok": "",
      "youtube": ""
    },
    "locks": [
      {
        "_id": "62c5b616e79ba598eeb6bd52",
        "unlockDate": "2022-03-22T10:14:00.000Z",
        "amount": 100,
        "providerId": "pinksale",
        "api": "pinksale",
        "lockId": "35282",
        "percent": 0.0010103184581873518,
        "type": "token"
      },
      {
        "_id": "62c5b616e79ba598eeb6bd53",
        "unlockDate": "2022-03-22T10:16:00.000Z",
        "amount": 20,
        "providerId": "pinksale",
        "api": "pinksale",
        "lockId": "35284",
        "percent": 0.00020206369163747035,
        "type": "token"
      },
      {
        "_id": "630922151a7aa643310bd043",
        "lockId": "5046",
        "unlockDate": "2022-05-14T09:37:35.000Z",
        "providerId": "team-finance",
        "api": "team-finance",
        "type": "token",
        "amount": 10531.038185289517,
        "percent": 0.10639702262473831
      }
    ],
    "logo": "3/bsc/0x0cbd6fadcf8096cc9a43d90b45f65826102e3ece.png?1696519781",
    "reprPair": {
      "id": {
        "chain": "bsc",
        "exchange": "dex091865",
        "pair": "0xf8104aaa719d31ea25dc494576593c10a8f929e6",
        "token": "0x0cbd6fadcf8096cc9a43d90b45f65826102e3ece",
        "tokenRef": "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c"
      },
      "updatedAt": "2024-07-27T14:46:05.483Z"
    },
    "banner": ""
  },
  "pair": {
    "_id": "62f6d81868fc706c1e07ac15",
    "id": {
      "chain": "bsc",
      "exchange": "sushi",
      "pair": "0x3d41ced5764340265d58ea4996f909eb05e25fdb",
      "token": "0x0cbd6fadcf8096cc9a43d90b45f65826102e3ece",
      "tokenRef": "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c"
    },
    "name": "CheckDot",
    "nameRef": "Wrapped BNB",
    "symbol": "CDT",
    "symbolRef": "WBNB",
    "type": "standard-pair",
    "creationBlock": 20388811,
    "creationTime": "2022-08-12T22:45:40.000Z",
    "team": {
      "wallet": "0x961a14beabd590229b1c68a21d7068c8233c8542"
    },
    "metrics": {
      "initialLiquidity": 1297.8,
      "liquidity": 44216.05553458308,
      "liquidityUpdatedAt": "2024-07-29T16:56:25.294Z",
      "reserve": 972.8739114636744,
      "reserveRef": 0.35946279716108176,
      "initialLiquidityUpdatedAt": "2022-08-12T22:45:40.000Z",
      "initialReserve": 37592.5,
      "initialReserveRef": 2
    },
    "locks": [],
    "dextScore": {
      "information": 99,
      "holders": 99,
      "pool": 23,
      "transactions": 99,
      "creation": 99,
      "total": 86
    },
    "periodStats": {
      "6h": {
        "volume": {
          "total": 87603.71808258654,
          "buys": 43801.49657544655,
          "sells": 43802.22150713998
        },
        "swaps": {
          "total": 2,
          "buys": 1,
          "sells": 1
        },
        "price": {
          "usd": {
            "first": 45.667741971018515,
            "last": 45.23590072722542,
            "min": 45.23590072722542,
            "max": 45.667741971018515,
            "diff": -0.9456154939019055
          },
          "chain": {
            "first": 0.07921644621059123,
            "last": 0.07846736322150541,
            "min": 0.07846736322150541,
            "max": 0.07921644621059123,
            "diff": -0.9456154939019126
          }
        },
        "liquidity": {
          "usd": {
            "first": 44218.027885411306,
            "last": 44216.05553458308,
            "min": 44216.05553458308,
            "max": 44218.027885411306,
            "diff": -0.004460512877998862
          }
        },
        "volatility": 1.9812648827091393,
        "makers": 1,
        "updatedAt": "2024-07-29T17:38:55.770Z"
      },
      "24h": {
        "volume": {
          "total": 87607.41496116665,
          "buys": 43803.91065463012,
          "sells": 43803.50430653653
        },
        "swaps": {
          "total": 11,
          "buys": 7,
          "sells": 4
        },
        "price": {
          "usd": {
            "first": 0.21980298607875826,
            "last": 45.23590072722542,
            "min": 0.2169557018380448,
            "max": 45.667741971018515,
            "diff": 20480.202996431
          },
          "chain": {
            "first": 0.0003771500796569458,
            "last": 0.07846736322150541,
            "min": 0.000372825593411923,
            "max": 0.07921644621059123,
            "diff": 20705.341813232288
          }
        },
        "liquidity": {
          "usd": {
            "first": 422.04382206150973,
            "last": 44216.05553458308,
            "min": 418.989827223199,
            "max": 44218.027885411306,
            "diff": 10376.650343702679
          }
        },
        "volatility": 1.9813484921251177,
        "makers": 8,
        "updatedAt": "2024-07-29T16:56:49.669Z"
      },
      "1h": {
        "volume": {
          "total": 0,
          "buys": 0,
          "sells": 0
        },
        "swaps": {
          "total": 0,
          "buys": 0,
          "sells": 0
        },
        "price": {
          "usd": {
            "first": 0,
            "last": 0,
            "min": 0,
            "max": 0,
            "diff": 0
          },
          "chain": {
            "first": 0,
            "last": 0,
            "min": 0,
            "max": 0,
            "diff": 0
          }
        },
        "liquidity": {
          "usd": {
            "first": 0,
            "last": 0,
            "min": 0,
            "max": 0,
            "diff": 0
          }
        },
        "volatility": 1.9812648827091393,
        "makers": 0,
        "updatedAt": "2024-07-29T17:59:35.797Z"
      },
      "5m": {
        "volume": {
          "total": 0,
          "buys": 0,
          "sells": 0
        },
        "swaps": {
          "total": 0,
          "buys": 0,
          "sells": 0
        },
        "price": {
          "usd": {
            "first": 0,
            "last": 0,
            "min": 0,
            "max": 0,
            "diff": 0
          },
          "chain": {
            "first": 0,
            "last": 0,
            "min": 0,
            "max": 0,
            "diff": 0
          }
        },
        "liquidity": {
          "usd": {
            "first": 0,
            "last": 0,
            "min": 0,
            "max": 0,
            "diff": 0
          }
        },
        "volatility": 1.9812648827091393,
        "makers": 0,
        "updatedAt": "2024-07-29T17:02:23.953Z"
      }
    }
  },
  "price": 45.23590072722542,
  "priceInterval": 0.21980298607875826,
  "priceDiff": 20480.202996431,
  "volume": 87607.41496116667,
  "swaps": 11
}