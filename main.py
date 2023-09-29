from solana.rpc.api import Client
from solana.rpc.types import TxOpts
from solana.account import Account
from solana.rpc.commitment import Confirmed
import json

# Установите нужные значения
nft_id = "Ваш NFT ID"
snapshot_date = "Дата снимка (YYYY-MM-DD)"
solana_endpoint = "https://api.mainnet-beta.solana.com"  # URL-адрес Сolana API

def get_token_accounts(nft_id):
    connection = Client(solana_endpoint)
    accounts = connection.get_program_accounts(nft_id, commitment=Confirmed)

    return accounts

def get_wallet_balances(accounts):
    wallet_balances = {}

    for account in accounts:
        wallet_address = str(account['pubkey'])
        balance = account['account']['lamports']
        wallet_balances[wallet_address] = balance

    return wallet_balances

def save_snapshot(snapshot):
    with open(f'snapshot_{snapshot_date}.json', 'w') as file:
        json.dump(snapshot, file, indent=4)

def main():
    accounts = get_token_accounts(nft_id)
    snapshot = get_wallet_balances(accounts)
    save_snapshot(snapshot)

if name == "main":
    main()