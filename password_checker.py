import requests
import hashlib
import sys

def request_api_data(query):
    url = 'https://api.pwnedpasswords.com/range/' + query
    res = requests.get(url) # establish connection and retrieve data
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check api and try again')
    return res    

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':')for line in hashes.text.splitlines()) # seperates hashes and the count from data received
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0
        
def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper() # converts the password you entered into hash using sha1 algorithm
    head = sha1password[:5] # captures first 5 letters of hashed password
    tail = sha1password[5:] # captures remaining letters (from 6th letter) of hashed password
    response = request_api_data(head) # call request_api_data function
    return get_password_leaks_count(response, tail) # call get_password_leaks_count function
        
def main(args):
    for password in args:
        count = pwned_api_check(password) # call pwned_api_check function
        if count:
            print(f'{password} was found {count} times..... you should probably change your password')
        else:
            print(f'{password} was not found. carry on!')
    return
    
if __name__ == '__main__':    
    main(sys.argv[1:])
        