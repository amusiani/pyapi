challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

print(challenge[2][1])

print(trial[2].get("eyes"))

print(nightmare[0].get("d"))

print("My",  challenge[2][1], "!",  "The", trial[2].get("eyes"), "do",  nightmare[0].get("d"))

