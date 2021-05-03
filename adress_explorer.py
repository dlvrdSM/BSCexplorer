from datetime import datetime
import requests
import schedule
import time


def token_balance(contract_address, wallet_address):
    '''Get the token balance for a certain address.'''
    api_key = '' 
    # The BSC API key is available for free 
    # at https://bscscan.com/myapikey after registering
    response = requests.get('https://api.bscscan.com/api?module=account&action=tokenbalance'
                           f'&contractaddress={contract_address}&address={wallet_address}&tag=latest&apikey={api_key}')
    result = response.json()['result']
    token_balance = int(result) / pow(10, 9) 
    
    return token_balance


contract =  '0x8076c74c5e3f5852037f31ff0093eeb8c8add8d3' # the Safemoon contract address
wallet = '0x0000000000000000000000000000000000000001' # the burn address


def job():
    now = datetime.now()
    current_date = now.strftime('%d/%m/%Y')
    current_time = now.strftime('%H:%M:%S')
    current_balance = token_balance(contract, wallet)
    with open('data.txt', 'a') as data:
        current_data = f'{current_date}, {current_time}, {current_balance}\n' 
        data.write(current_data)

        
schedule.every().hour.at(':00').do(job)
        
    
while True:
    schedule.run_pending()
    time.sleep(1)
