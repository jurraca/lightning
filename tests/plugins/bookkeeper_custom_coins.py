#!/usr/bin/env python3
from pyln.client import Plugin


plugin = Plugin()


UTXO_DEPOSIT_TAG = "utxo_deposit"
UTXO_SPENT_TAG = "utxo_spent"


@plugin.method("sendspend")
def emit_spend(plugin, acct, outpoint, txid, amount, **kwargs):
    """Emit a 'utxo_spent' movement
    """
    utxo_spent = {
            "account": acct,
            "outpoint": outpoint,
            "spending_txid": txid,
            "amount_msat": amount,
            "coin_type": "bcrt",
            "timestamp": 1679955976,
            "blockheight": 111,
    }
    plugin.notify(UTXO_SPENT_TAG, {UTXO_SPENT_TAG: utxo_spent})


@plugin.method("senddeposit")
def emit_deposit(plugin, acct, is_withdraw, outpoint, amount, **kwargs):
    """Emit a 'utxo_deposit' movement
    """
    transfer_from = None

    if is_withdraw:
        acct = "external"
        tranfer_form = acct

    utxo_deposit = {
            "account": acct,
            "transfer_from": transfer_from,
            "outpoint": outpoint,
            "amount_msat": amount,
            "coin_type": "bcrt",
            "timestamp": 1679955976,
            "blockheight": 111,
    }
    plugin.notify(UTXO_DEPOSIT_TAG, {UTXO_DEPOSIT_TAG: utxo_deposit})


plugin.add_notification_topic(UTXO_DEPOSIT_TAG)
plugin.add_notification_topic(UTXO_SPENT_TAG)
plugin.run()
