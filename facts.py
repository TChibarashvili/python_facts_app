user1 = str("devopsboy")
pass1 = str(user1 + "123")

user2 = str("linuxboy")
pass2 = str(user2 + "123")

user3 = str("networkboy")
pass3 = str(user3 + "123")

secret = 123
user = temo

themes = ["f1_facts", "football_facts", "basketball_facts", "science_facts", "IT", "Random"]

f1_facts = ["",
            "Recording 365,000 spectators, the 2021 British Grand Prix broke attendance records.",
            "Over 400 million people watch Formula One on television.",
            "Netflix’s Formula One documentary series boosted viewership numbers in the US.",
            "The 2021 season-opening Bahrain Grand Prix broke viewership records on Sky Sports.",
            "Formula 1 saw a 99% increase in engagement on social media.",
            "Lewis Hamilton and Michael Schumacher have won seven titles each.",
            "Michael Schumacher had the fastest lap in 77 races.",
            "Lewis Hamilton has the most Grand Prix victories.",
            "52 F1 drivers have died while testing, practising, qualifying or racing F1.",
            "Ferrari is the absolute leader in Formula One."]

football_facts = ["",
                  "Football is the most popular sport in the world.",
                  "It was invented in China around 476 B.C.",
                  "More than 3.5 billion people watch the FIFA World Cup.",
                  "The fastest goal ever scored took only 2.4 seconds.",
                  "The fastest goal ever scored took only 2.4 seconds.",
                  "Only 8 countries have won the World Cup.",
                  "The first international game ever was played in 1872.",
                  "The largest football stadium is located in North Korea.",
                  "Premier League is ranked as the best football league.",
                  "Football players run on average 9.65 km every game."]

basketball_facts = ["",
                    "James Naismith invented basketball.",
                    "Basketball was played with a different ball.",
                    "Dribbling wasn't allowed in Basketball.",
                    "The 1979 NCAA tournament was the start of basketball greats.",
                    "Michael Jordan paid fines for wearing his shoes.",
                    "The first basketball game in Europe was arranged by Mel Rideout in Paris.",
                    "The official rim height for NBA, WNBA, FIBA, and NCAA courts is set at 10 ft or 3.05 meters.",
                    "Basketball is the national sport of Lithuania.",
                    "Basketball was played with a soccer ball.",
                    "Basketball Started Without a Name ."]

science_facts = ["",
                 "Babies have around 100 more bones than adults.",
                 "The Eiffel Tower can be 15 cm taller during the summer.",
                 "20% of Earth’s oxygen is produced by the Amazon rainforest.",
                 "Some metals are so reactive that they explode on contact with water.",
                 "Hawaii moves 7.5cm closer to Alaska every year.",
                 "In 2.3 billion years it will be too hot for life to exist on Earth.",
                 "Polar bears are nearly undetectable by infrared cameras.",
                 "It takes 8 minutes, 19 seconds for light to travel from the Sun to the Earth.",
                 "Stomach acid is strong enough to dissolve stainless steel.",
                 "Venus is the only planet to spin clockwise."]

IT_facts = ["",
            "Over 6,000 new computer viruses are created and released every month. 90% of emails contain some of them!",
            "The Firefox logo isn’t a fox… it’s a red panda!",
            "Samsung is 38 years and 1 month older than Apple.",
            "The name for “robot” has dark origins.",
            "Domain name registration used to be free.",
            "On average, people read 10% slower from a screen than from paper.",
            "The first computer mouse was made in 1964 by Doug Engelbart. It was rectangular and made from wood!",
            "On average, there is only one reply per 12 million spam emails sent.",
            "NASA’s internet speed is 91 GB per second.",
            "Until 2010, carrier pigeons were faster than the internet."]

random_facts = ["",
                "Competitive art used to be in the Olympics.",
                "A chef's hat has exactly 100 pleats.",
                "Some cats are actually allergic to humans.",
                "The majority of your brain is fat",
                "There was a successful Tinder match in Antarctica in 2014.",
                "There is a fruit that tastes like chocolate pudding.",
                "Too much water can kill you.",
                "The hottest temperature ever recorded on Earth was 2 billion degrees kelvin.",
                "The hottest inhabited place in the world is in Ethiopia.",
                "Hot water freezes faster than cold water."]

username = input("Enter Your Username: ")
password = input("Enter Your Password: ")

if username == user1 and password == pass1:
    print("Log In Successful !")
elif username == user2 and password == pass2:
    print("Log In Successful !")
elif username == user3 and password == pass3:
    print("Log In Successful !")
else:
    print("Incorrect Credentials !")

print(" Welcome To Facts.com ")
print(themes)
choice = str(input("Please Choose Desired Theme: "))
print("\nYour Desired Theme is " + choice + " !")

factnum = int(input("\nChoose Number from 1 to 10 to see fact about your Desired Theme: "))

if choice == str("science_facts") and 0 <= factnum <= 10:
    print(science_facts[factnum])
elif choice == str("science_facts") and factnum < 0 or factnum > 10:
    print("Invalid Number !")
else:
    pass

if choice == str("football_facts") and 0 <= factnum <= 10:
    print(football_facts[factnum])
elif choice == str("football_facts") and factnum < 0 or factnum > 10:
    print("Invalid Number !")
else:
    pass

if choice == str("f1_facts") and 0 <= factnum <= 10:
    print(f1_facts[factnum])
elif choice == str("f1_facts") and factnum < 0 or factnum > 10:
    print("Invalid Number !")
else:
    pass

if choice == str("basketball_facts") and 0 <= factnum <= 10:
    print(basketball_facts[factnum])
elif choice == str("basketball_facts") and factnum < 0 or factnum > 10:
    print("Invalid Number !")
else:
    pass

if choice == str("IT_facts") and 0 <= factnum <= 10:
    print(IT_facts[factnum])
elif choice == str("IT_facts") and factnum < 0 or factnum > 10:
    print("Invalid Number !")
else:
    pass

if choice == str("random_facts") and 0 <= factnum <= 10:
    print(random_facts[factnum])
elif choice == str("random_facts") and factnum < 0 or factnum > 10:
    print("Invalid Number !")
else:
    pass
