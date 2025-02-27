users = [
    {"email": "alice@example.com", "verified": True},
    {"email": "bob@example.com", "verified": False},
    {"email": "charlie@example.com", "verified": True},
    {"email": "daisy@example.com", "verified": False}
]

# Filter the verified users
verified_emails = [user for user in users if user['verified']]

# Print the email addresses of verified users
for user in verified_emails:
    print(user['email'])


users = [
    {"email": "alice@example.com", "verified": True},
    {"email": "bob@example.com", "verified": False},
    {"email": "charlie@example.com", "verified": True},
    {"email": "daisy@example.com", "verified": False}
]

# Filter the verified users
verified_users = filter(lambda user: user['verified'], users)

# Extract and print the email addresses of verified users
verified_emails = [user['email'] for user in verified_users]
print(verified_emails)