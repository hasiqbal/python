# ips = ['100.122.133.105', '100.122.133.111']

# Copy-paste the ips list in a .py file and extend the program so it:

# 1. Prompts the user to input an index (e.g, 0 or 1).

# 2. Returns the IP address that has that index.

user_prompt = "enter an index:"
ips = ['100.122.133.105', '100.122.133.111']

for i in ips:
    prompt = int(input(user_prompt)) - 1
    print( "you chose:",ips[prompt])
