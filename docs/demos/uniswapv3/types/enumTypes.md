---
id: enum-types
title: Enum Types
---


### ChainId

_Ethereum chain supported by the wrapper_

```graphql
enum ChainId {
  MAINNET
  ROPSTEN
  RINKEBY
  GOERLI
  KOVAN
  OPTIMISM
  OPTIMISTIC_KOVAN
  ARBITRUM_ONE
  ARBITRUM_RINKEBY
  POLYGON
  POLYGON_MUMBAI
}
```

### FeeAmount

_Pool swap fee amount_

```graphql
enum FeeAmount {
  LOWEST
  LOW
  MEDIUM
  HIGH
}
```

### PermitV

_Valid v value of Permit_

```graphql
enum PermitV {
  v_0
  v_1
  v_27
  v_28
}
```

### TradeType

_Type of trade, either exact input or exact output_

```graphql
enum TradeType {
  EXACT_INPUT
  EXACT_OUTPUT
}
```
