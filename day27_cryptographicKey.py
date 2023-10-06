'''
Day 27 of '30 days of 30
Programs challenege 
'''

'''
Use Crypto Module 
Generate a random
cryptographic key:

'''

import secrets

key = secrets.token_hex(16)
print(f"Random key: {key}")