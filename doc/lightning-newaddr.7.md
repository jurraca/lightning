lightning-newaddr -- Command for generating a new address to be used by Core Lightning
======================================================================================

SYNOPSIS
--------

**newaddr** [ *addresstype* ]

DESCRIPTION
-----------

The **newaddr** RPC command generates a new address which can
subsequently be used to fund channels managed by the Core Lightning node.

The funding transaction needs to be confirmed before funds can be used.

*addresstype* specifies the type of address wanted; i.e. *p2sh-segwit*
(e.g. `2MxaozoqWwiUcuD9KKgUSrLFDafLqimT9Ta` on bitcoin testnet or
`3MZxzq3jBSKNQ2e7dzneo9hy4FvNzmMmt3` on bitcoin mainnet) or *bech32*
(e.g. `tb1qu9j4lg5f9rgjyfhvfd905vw46eg39czmktxqgg` on bitcoin testnet
or `bc1qwqdg6squsna38e46795at95yu9atm8azzmyvckulcc7kytlcckxswvvzej` on
bitcoin mainnet). The special value *all* generates both address types
for the same underlying key.

If no *addresstype* is specified the address generated is a *bech32* address.

To send an on-chain payment _from_ the Core Lightning node wallet, use `withdraw`. 

RETURN VALUE
------------

[comment]: # (GENERATE-FROM-SCHEMA-START)
On success, an object is returned, containing:
- **bech32** (string, optional): The bech32 (native segwit) address
- **p2sh-segwit** (string, optional): The p2sh-wrapped address

[comment]: # (GENERATE-FROM-SCHEMA-END)

ERRORS
------

If an unrecognized address type is requested an error message will be
returned.

AUTHOR
------

Felix <<fixone@gmail.com>> is mainly responsible.

SEE ALSO
--------

lightning-listfunds(7), lightning-fundchannel(7), lightning-withdraw(7), lightning-listtransactions(7)

RESOURCES
---------

Main web site: <https://github.com/ElementsProject/lightning>

[comment]: # ( SHA256STAMP:550089858649865ed4d23384dcc5deeef314f5a1976a9610e611dbe17c1063d6)
