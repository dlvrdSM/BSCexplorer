import requests

def token_balance(contract_address, wallet_address):
    '''Get the token balance for a certain address.'''
    response = requests.get('https://api.bscscan.com/api?module=account&action=tokenbalance'
                           f'&contractaddress={contract_address}&address={wallet_address}&tag=latest&apikey={api_key}')
    # extract the balance string from the dictionary
    result = response.json()['result']
    # convert the result string to an integer and show it with che correct unit
    balance = int(result) / pow(10, 9)
    return balance
