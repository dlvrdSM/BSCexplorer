import requests

def token_balance(contract_address, wallet_address):
    '''Get the token balance for a certain address.'''
    response = requests.get('https://api.bscscan.com/api?module=account&action=tokenbalance'
                           f'&contractaddress={contract_address}&address={wallet_address}&tag=latest&apikey={api_key}')
    result = response.json()['result']
    token_balance = int(result) / pow(10, 9) 
    
    return token_balance
