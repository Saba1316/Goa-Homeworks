# Codewars 8 kyu: 
# Generate user links


from urllib.parse import quote


def generate_link(user: str) -> str:
    return f"http://www.codewars.com/users/{quote(user)}"