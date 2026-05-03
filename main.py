print("hello! I am an AI Bot. What is your name ?")
name = input()
print(f"nice to meet you , {name}!")
print("how are you feeling today ? (good / bad)")
mood = input().lower()
if mood == "good":
    print("i am glad to hear that!")
elif mood == "bad":
    print("im sorry to hear that ! i hope you feel better soon")
else:
    print("i see . sometimes it is really hard to put your felling into words")
print(f"it was really nice chatting to you {name}. BYEEEEE!!!!!!!!!!!!!")