# import random module 
import random 

subjects = [
    "aamir khan",
    "imran khan",
    "shahrukhan",
    "salman khan",
    "kamal khan",
    "shahid afridi",
    "nawaz sharif",
    "anwar saeed",
]

actions = [
    "announced a new project",
    "was spotted at a secret meeting",
    "surprised fans with a big decision",
    "shared an unexpected statement",
    "made headlines after a bold move",
    "revealed shocking news",
    "trended on social media"
]


places_or_events = [
    "in Lahore",
    "in Karachi",
    "in Islamabad",
    "at a private event",
    "during a live interview",
    "at a press conference",
    "on social media",
    "at an international summit"
]
# start the headline generation loop

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_events)

    headline = f"Breaking News:{subject} {action} {place_or_thing}"

    print("\n" + headline)

    user = input("\n do you want another headline? (Yes or no)").strip().lower()

    if user == "no" :
        break

# print final good by 

print("\n thanks for using fake headline generate programmer")
