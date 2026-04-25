import re

# Rules
rules = [
    (r"parent\((.*),(.*)\)", "child(\\2,\\1)")
]

def apply_rules(user_input):
    for pattern, response in rules:
        match = re.match(pattern, user_input)
        if match:
            return response.replace("\\1", match.group(1)).replace("\\2", match.group(2))
    return "I can only understand parent(x,y) format"

# Chat loop
while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    print("Bot:", apply_rules(user))
