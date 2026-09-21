import re

text = """
Hello, my email is anokhi@gmail.com.
You can contact mitadt@yahoo.com.
My college email is anokhi123@gmail.com.
For support, contact support@company.org.
"""

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = re.findall(pattern, text)

print("Email addresses found:")

for email in emails:
    print(email)