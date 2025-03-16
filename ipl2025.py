import random

def display_rules():
    print("\n🏏 WELCOME TO THE ULTIMATE IPL QUIZ! 🏏\n")
    print("This game consists of **3 rounds**: \n")
    print("1️⃣ **Guess the IPL Team** – Identify the correct IPL team based on a player.\n")
    print("2️⃣ **Guess the Head Coach** – Identify the head coach of an IPL team.\n")
    print("3️⃣ **Foreign Player Country Guess** – Identify the correct country of a foreign player.\n")
    print("🔹 In **Round 1**, you will answer 11 questions. If you get **9 or more correct**, you proceed to Round 2.\n")
    print("🔹 In **Round 2**, you will answer 3 questions. If you get **2 or more correct**, you proceed to Round 3.\n")
    print("🔹 In **Round 3**, you will answer 5 questions. If you get **4 or more correct**, you are declared **IPL GURU 2025!** 🎉\n")
    print("Let's start! 🚀\n")

def guess_ipl_team():
    teams = {
        "Chennai Super Kings": {"players": ["MS Dhoni", "Ruturaj Gaikwad", "Ravindra Jadeja", "Andre Siddharth", "Shaik Rasheed", "Rahul Tripathi", "Shivam Dube", "Rachin Ravindra", "Deepak Hooda", "Vijay Shankar", "Ramakrishna Ghosh", "Anshul Kamboj", "Sam Curran", "Ravichandran Ashwin", "Devon Conway", "Vansh Bedi", "Jamie Overton", "Kamlesh Nagarkoti", "Shreyas Gopal", "Matheesha Pathirana", "Mukesh Choudhary", "Nathan Ellis", "Gurjapneet Singh", "Noor Ahmad", "Khaleel Ahmed"], "logo": "🟨 CSK", "hint": "Famous for filter coffee and Marina Beach."},
        "Delhi Capitals": {"players": ["Faf du Plessis", "Karun Nair", "Jake Fraser-McGrk", "Sameer Rizvi", "Ashutosh Sharma", "Tripurana Vijay", "Vipraj Nigam", "Axar Patel", "Darshan Nalkande", "Ajay Jadav Mandal", "Manvanth Kumar L", "Madhav Tiwari", "Tristian Stubbs", "Abhishek Porel", "Donovan Ferreira", "KL Rahul", "Kuldeep Yadav", "Dushmantha Chameera", "Mitchell Starc", "Mohit Sharma", "T Natarajan", "Mukesh Kumar"], "logo": "🔵 DC", "hint": "Known for Chole Bhature and India Gate."},
        "Gujarat Titans": {"players": ["Shubman Gill", "Sai Sudharsan", "Glenn Philips", "Sharukh Khan", "Rahul Tewatia", "Nishant Sindhu", "Sherfane Rutherford", "Mahipal Lomror", "Rashid Khan", "Ravisrinivasan Sai Kishore", "Arshad Khan", "Jayant Yadav", "Karim Janat", "Washington Sundar", "Kumar Kushagra", "Anuj Rawat", "Jos Buttler", "Gerald Coetzee", "Manav Suthar", "Gurnoor Brar", "Ishant Sharma", "Kagiso Rabada", "Kulwant Khejroliya", "Prasidh Krishna", "Mohammed Siraj"], "logo": "🔷 GT", "hint": "Home of Dhokla and the Statue of Unity."},
        "Kolkata Knight Riders": {"players": ["Ajinkya Rahane", "Manish Pandey", "Rinku Singh", "AngKrish Raghuvanshi", "Rovman Powell", "Anukul Roy", "Ramandeep Singh", "Venkatesh Iyer", "Moeen Ali", "Andre Russell", "Sunil Narine", "Quinton de Kock", "Rahmanullah Gurbaz", "Luvnith Sisodia", "Varun Chakaravarthy", "Mayank Markande", "Vaibhav Arora", "Harshit Rana", "Anrich Nortje", "Umran Malik", "Spencer Johnson"], "logo": "🟣 KKR", "hint": "Rosogolla and Howrah Bridge make this place iconic."},
        "Lucknow Super Giants": {"players": ["Himmat Singh", "David Miller", "Aiden Markram", "Ayush Badoni", "Mitchell Marsh", "Abdul Samad", "Arshin Kulkarni", "Yuvraj Chaudhary", "Shahbaz Ahmed", "RS Hangargekar", "Matthew Breetzke", "Nicholas Pooran", "Aryan Juyal", "Rishabh Pant", "Ravi Bishnoi", "Mayank Yadav", "Akash Deep", "Manimaran Siddharth", "Shamar Joseph", "Avesh Khan", "Prince Yadav", "Mohsin Khan", "Akash Maharaj Singh", "Digvesh Rathi"], "logo": "🟥 LSG", "hint": "City of Nawabs, famous for Tunday Kababi."},
        "Mumbai Indians": {"players": ["Rohit Sharma", "Suryakumar Yadav", "Jasprit Bumrah", "Tilak Varma", "Naman Dhir", "Bevon Jacobs", "Hardik Pandya", "Raj Bawa", "Will Jacks", "Vignesh Puthur", "Satyanarayana Raju", "Mitchell Santner", "Arjun Tendulkar", "Corbin Bosch", "Ryan Rickelton", "Krishnan Shrijith", "Robin Minz", "Ashwani Kumar", "Reece Topley", "Karn Sharma", "Trent Boult", "Deepak Chahar", "Mujeeb Ur Rahman"], "logo": "🔵 MI", "hint": "Vada Pav and Bollywood stars belong here."},
        "Punjab Kings": {"players": ["Nehal Wadhera", "Harnoor Singh", "Shreyas Iyer", "Pyla Avinash", "Priyansh Arya", "Musheer Khan", "Marcus Stoinis", "Glenn Maxwell", "Aaron Hardie", "Suryansh Shedge", "Shashank Singh", "Praveen Dubey", "Azmatullah Omarzai", "Marco Jansen", "Prabhsimran Singh", "Josh Inglish", "Vishnu Vinod", "Harpreet Brar", "Lockie Ferguson", "Arshdeep Singh", "Yuzvendra Chahal", "Vijaykumar Vyshak", "Kuldeep Sen", "Yash Thakur", "Xavier Bartlett"], "logo": "🟡 PBKS", "hint": "Land of Butter Chicken and Bhangra beats."},
        "Rajasthan Royals": {"players": ["Sanju Samson", "Vaibhav Suryavanshi", "Shimron Hetmyer", "Yashasvi Jaiswal", "Shubham Dubey", "Nitish Rana", "Riyan Parag", "Yudhvir Singh Charak", "Wanindu Hasaranga", "Dhruv Jurel", "Kunal Singh Rathore", "Sandeep Sharma", "Tushar Deshpande", "Kumar Karthikeya", "Akash Madhwal", "Kwena Maphaka", "Maheesh Theekshana", "Fazalhaq Farooqi", "Ashok Sharma", "Jofra Archer"], "logo": "🎀 RR", "hint": "Famous for Dal Baati Churma and Hawa Mahal."},
        "Royal Challengers Bangalore": {"players": ["Virat Kohli", "Rajat Patidar", "Devdutt Padikkal", "Swastik Chikara", "Tim David", "Krunal Pandya", "Liam Livingstone", "Manoj Bhandage", "Jacob Bethell", "Romario Shepherd", "Swapnil Singh", "Mohit Rathee", "Philip Salt", "Jitesh Sharma", "Josh Hazlewood", "Bhuvneshwar Kumar", "Lungi Ngidi", "Rasikh Dar Salam", "Suyash Sharma", "Yash Dayal", "Nuwan Thushara", "Abhinandan Singh"], "logo": "🟥 RCB", "hint": "Land of Masala Dosa and Electronic City."},
        "Sunrisers Hyderabad": {"players": ["Atharva Taide", "Travis Head", "Abhinav Manohar", "Sachin Baby", "Aniket Verma", "Nitish Kumar Reddy", "Abhishek Sharma", "Kamindu Mendis", "Wiaan Mulder", "Heinrich Klaasen", "Ishan Kishan", "Zeeshan Ansari", "Pat Cummins", "Mohammed Shami", "Harshal Patel", "Rahul Chahar", "Simarjeet Singh", "Eshan Malinga", "Adam Zampa", "Jaydev Unadkat"], "logo": "🟧 SRH", "hint": "Biryani and Charminar make this place special."}
    }
    team, data = random.choice(list(teams.items()))
    player = random.choice(data["players"])

    # Generate options with the correct answer and 3 wrong teams
    options = random.sample([t for t in teams.keys() if t != team], 3) + [team]
    random.shuffle(options)

    # Display question
    print(f"\nGuess the IPL team for this player: {player}")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    # Get user input and validate
    try:
        answer = int(input("Enter your choice (1-4): "))
        if 1 <= answer <= 4:
            chosen_team = options[answer - 1]
            if chosen_team == team:
                print(f"✅ Correct! {player} plays for {team} {data['logo']}")
                return True
            else:
                print(f"❌ Wrong! {player} actually plays for {team} {data['logo']}")
                return False
        else:
            print("Invalid input! Please enter a number between 1 and 4.")
            return False
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return False

def guess_head_coach():
    coaches = {
        "CSK": {"name": "Stephen Fleming", "logo": "🟨 CSK", "hint": "Famous for filter coffee and Marina Beach."},
        "DC": {"name": "Hemang Badani", "logo": "🔵 DC", "hint": "Known for Chole Bhature and India Gate."},
        "GT": {"name": "Ashish Nehra", "logo": "🔷 GT", "hint": "Home of Dhokla and the Statue of Unity."},
        "KKR": {"name": "Chandrakanth Pandit", "logo": "🟣 KKR", "hint": "Rosogolla and Howrah Bridge make this place iconic."},
        "LSG": {"name": "Justin Langer", "logo": "🟥 LSG", "hint": "City of Nawabs, famous for Tunday Kababi."},
        "MI": {"name": "Mahela Jayawardene", "logo": "🔵 MI", "hint": "Vada Pav and Bollywood stars belong here."},
        "PBKS": {"name": "Ricky Ponting", "logo": "🟡 PBKS", "hint": "Land of Butter Chicken and Bhangra beats."},
        "RR": {"name": "Rahul Dravid", "logo": "🎀 RR", "hint": "Famous for Dal Baati Churma and Hawa Mahal."},
        "RCB": {"name": "Andy Flower", "logo": "🟥 RCB", "hint": "Land of Masala Dosa and Electronic City."},
        "SRH": {"name": "Daniel Vettori", "logo": "🟧 SRH", "hint": "Biryani and Charminar make this place special."}
    }

    team, coach = random.choice(list(coaches.items()))
    print(f"\nGuess the head coach of {team}:")
    options = random.sample([c["name"] for c in coaches.values() if c["name"] != coach["name"]], 3) + [coach["name"]]
    random.shuffle(options)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    answer = int(input("Enter your choice (1-4): "))
    return options[answer - 1] == coach["name"]

def guess_foreign_player_country():
    players = {
        "🇦🇺 Australia": ["Nathan Ellis", "Spencer Johnson", "Travis Head", "Pat Cummins", "Adam Zampa", "Tim David", "Josh Hazlewood", "Jake Fraser-McGurk", "Mitchell Starc", "Marcus Stoinis", "Glenn Maxwell", "Aaron Hardie", "Jos Inglis", "Xavier Bartlett", "Mitchell Marsh"],
        "🇳🇿 New Zealand": ["Rachin Ravindra", "Devon Conway", "Lockie Ferguson", "Bevon Jacobs", "Mitchell Santner", "Trent Boult", "Glenn Phillips"],
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿 England": ["Sam Curran", "Jamie Overton", "Jofra Archer", "Moeen Ali", "Liam Livingstone", "Philip Salt", "Jacob Bethell", "Will Jacks", "Reece Topley", "Jos Buttler"],
        "🇿🇦 South Africa": ["Kwena Maphaka", "Quinton de Kock", "Anrich Nortje", "Wiaan Mulder", "Heinrich Klaasen", "Lungi Ngidi", "Faf du Plessis", "Tristan Stubbs", "Donovan Ferreira", "Marco Jansen", "Corbin Bosh", "Ryan Rickelton", "Gerald Coetzee", "Kagiso Rabada", "David Miller", "Aiden Markram", "Matthew Breetzke"],
        "🇦🇫 Afghanistan": ["Noor Ahmad", "Fazalhaq Farooqi", "Rahmanullah Gurbaz", "Azmatullah Omarzai", "Mujeeb Ur Rahman", "Rashid Khan", "Karim Janat"],
        "🇱🇰 Sri Lanka": ["Matheesha Pathirana", "Wanindu Hasaranga", "Maheesh Theekshana", "Kamindu Mendis", "Eshan Malinga", "Nuwan Thushara", "Dushmantha Chameera"],
        "🇻🇨 West Indies": ["Shimron Hetmyer", "Rovman Powell", "Sunil Narine", "Andre Russell", "Romario Shepherd", "Sherfane Rutherford", "Nicholas Pooran", "Shamar Joseph"]
    }

    country, player_list = random.choice(list(players.items()))
    player = random.choice(player_list)
    print(f"\nWhich country does {player} belong to?")
    options = random.sample([c for c in players.keys() if c != country], 3) + [country]
    random.shuffle(options)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    answer = int(input("Enter your choice (1-4): "))
    return options[answer - 1] == country

def play_quiz():
    display_rules()
    
    # Round 1: Guess the IPL Team
    print("\n🔥 ROUND 1: Guess the IPL Team 🔥")
    round1_score = 0
    for _ in range(11):
        if guess_ipl_team():
            round1_score += 1
        print(f"Your current score: {round1_score}/11\n")
    
    if round1_score >= 9:
        print("🎉 Congratulations! You have qualified for Round 2! 🎉")
    else:
        print("❌ You did not qualify for Round 2. Better luck next time! ❌")
        return
    
    # Round 2: Guess the Head Coach
    print("\n🔥 ROUND 2: Guess the Head Coach 🔥")
    round2_score = 0
    for _ in range(3):
        if guess_head_coach():
            round2_score += 1
        print(f"Your current score: {round2_score}/3\n")
    
    if round2_score >= 2:
        print("🎉 Congratulations! You have qualified for Round 3! 🎉")
    else:
        print("❌ You did not qualify for Round 3. Better luck next time! ❌")
        return
    
    # Round 3: Foreign Player Country Guess
    print("\n🔥 ROUND 3: Foreign Player Country Guess 🔥")
    round3_score = 0
    for _ in range(5):
        if guess_foreign_player_country():
            round3_score += 1
        print(f"Your current score: {round3_score}/5\n")
    
    if round3_score >= 4:
        print("\n🎉 YOU ARE NOW 'IPL GURU 2025'! 🏆🏏")
    else:
        print("\nYou couldn't score 4 or more in the final round. Better luck next time! 🔄")

play_quiz()