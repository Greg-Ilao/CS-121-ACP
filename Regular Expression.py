import re

text = "My phone is 9876543210 and email is test@gmail.com"


number = re.search(r"\d{10}", text)
print("Phone:", number.group())


words = re.findall(r"\w+", text)
print("Words:", words)


parts = re.split(r"[ ,]", text)
print("Split:", parts)


masked = re.sub(r"\d", "X", text)
print("Masked:", masked)


email = "example@mail.com"
print("Email valid?:", bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)))
