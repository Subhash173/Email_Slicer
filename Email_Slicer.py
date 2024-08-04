
# Define a function to slice the email
def email_slicer(email):
    
    # Find the position of '@' in the email address
    at_position = email.find('@')
    
    # Extract the username (everything before '@')
    username = email[:at_position]
    
    # Extract the domain (everything after '@')
    domain = email[at_position + 1:]
    
    return username, domain

# Take the email address as input from the user
email_address = input("Enter your email address: ")

# Call the email_slicer function and get the username and domain
username, domain = email_slicer(email_address)

# Display the username and domain
print(f"Username: {username}")
print(f"Domain: {domain}")
