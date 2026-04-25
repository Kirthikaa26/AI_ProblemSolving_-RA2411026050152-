import re

rules = [
    (r"parent\((.*),(.*)\)", "child(\\2,\\1)"),
    (r"father\((.*),(.*)\)", "parent(\\1,\\2)"),
    (r"mother\((.*),(.*)\)", "parent(\\1,\\2)")
]

def apply_rules(user_input):
    for pattern, response in rules:
        match = re.match(pattern, user_input)
        if match:
            res = response
            for i in range(1, len(match.groups()) + 1):
                res = res.replace(f"\\{i}", match.group(i))
            return res
    return "No rule matched"

print("AI Chatbot Started (type exit to stop)")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    print("Bot:", apply_rules(user))
