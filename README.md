# password_checker
This Python script checks if a given password has been compromised in data breaches using the Have I Been Pwned API. The script takes one or more passwords as command-line arguments and queries the API to check if each password has been exposed in previous breaches.

Here's a breakdown of how the script works:

1. The `request_api_data` function constructs the API URL with the first five characters of the SHA-1 hash of the password and sends a GET request to the Have I Been Pwned API. If the response status code is not 200, it raises a `RuntimeError`.

2. The `get_password_leaks_count` function takes the response from the API, which contains a list of hashes and their corresponding counts, and checks if the hash of the password to be checked is present. If found, it returns the count; otherwise, it returns 0.

3. The `pwned_api_check` function calculates the SHA-1 hash of the password, extracts the first five characters (head) and the remaining characters (tail), calls `request_api_data` to get the response, and then calls `get_password_leaks_count` to check if the password hash is present and returns the count.

4. The `main` function takes command-line arguments (passwords) and iterates through each one, calling `pwned_api_check` for each password. If the count is non-zero, it suggests changing the password due to potential compromises; otherwise, it indicates that the password was not found.

5. The script is executed only if it's the main module, taking passwords from the command line.

To use the script, you would run it from the command line, providing passwords as arguments. For example:

```bash
python script_name.py password1 password2 password3
```

The script then checks each password against the Have I Been Pwned API and informs you if any of them have been compromised.