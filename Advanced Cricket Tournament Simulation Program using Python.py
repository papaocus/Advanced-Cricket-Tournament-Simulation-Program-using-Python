#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random 

class Player:
    def __init__(self, name, bowling, batting, fielding, running, experience):
        """
        Represents a player in a cricket team.
        Initialize a Player object with the provided attributes.
        
        Args:
            name (str): The name of the player.
            bowling (float): The bowling skill of the player.
            batting (float): The batting skill of the player.
            fielding (float): The fielding skill of the player.
            running (float): The running skill of the player.
            experience (float): The experience level of the player.
        """
        self.name = name 
        self.bowling = bowling 
        self.batting = batting 
        self.fielding = fielding 
        self.running = running 
        self.experience = experience


# In[2]:


class Team:

    def __init__(self, name, players):
        """
        Initialize a Team object with the provided attributes.
        
        Args:
            name (str): The name of the team.
            players (list): The list of Player objects representing the team's players.
        """
        self.name = name 
        self.players = players 
        self.captain = None 
        self.batting_order = players.copy()
        self.bowlers = []

    def select_captain(self, captain):
        """
        Select the captain for the team.
        
        Args:
            captain (Player): The Player object representing the captain of the team.
        """
        self.captain = captain

    def sending_next_player(self):
        """
        Send the next player from the batting order.
        
        Returns:
            Player or None: The next Player object from the batting order, or None if the batting order is empty.
        """
        if len(self.batting_order)>0:
            return self.batting_order.pop(0)
        return None 
    
    def choose_bowler(self):
        """
        Choose a bowler randomly from the team's bowlers.
        
        Returns:
            Player: The Player object representing the chosen bowler.
        """
        return random.choice(self.bowlers)
    
    def decide_batting_order(self):
        # Sort the players in descending order of batting skill
        self.batting_order = sorted(self.players, key=lambda player: player.batting, reverse=True)

    def choose_bowlers(self):
        # Sort the players in descending order of bowling skill
        self.bowlers = sorted(self.players, key=lambda player: player.bowling, reverse=True)
    


# In[3]:


class Field:
    def __init__(self, size, fan_ratio, pitch_conditions, home_advantage):
        """
        Initialize a Field object with the provided attributes.
        
        Args:
            size (str): The size of the field.
            fan_ratio (float): The fan ratio of the field.
            pitch_conditions (float): The pitch conditions of the field.
            home_advantage (float): The home advantage of the field.
        """
        self.size = size
        self.fan_ratio = fan_ratio
        self.pitch_conditions = pitch_conditions
        self.home_advantage = home_advantage


# In[4]:


class Umpire:
    def __init__(self, field):
        """
        Initialize an Umpire object with the provided attributes.
        
        Args:
            field (Field): The Field object representing the field conditions.
        """
        self.field = field
        self.scores = 0
        self.wickets = 0
        self.overs = 0

    def update_score(self, runs):
        """
        Update the score based on the runs scored.
        
        Args:
            runs (int): The runs scored in the ball.
        """
        self.scores += runs

    def update_wickets(self):
        """
        Update the wickets count.
        """
        self.wickets += 1

    def update_overs(self):
        """
        Update the overs count.
        """
        self.overs += 1

    def predict_outcome(self, batsman, bowler):
        """
        Predict the outcome of a ball based on batsman and bowler stats.
        
        Args:
            batsman (Player): The Player object representing the batsman.
            bowler (Player): The Player object representing the bowler.
        
        Returns:
            str: The outcome of the ball (either "OUT" or "NOT OUT").
        """
        batting_prob = batsman.batting * self.field.pitch_conditions * random.random()
        bowling_prob = bowler.bowling * self.field.pitch_conditions * random.random()
        if batting_prob > bowling_prob:
            return "OUT"
        return "NOT OUT"
    def handle_lbw(self, batsman, bowler):
        # Implement logic to handle LBWs
        lbw_threshold = 0.7  # Adjust this threshold as needed
        lbw_chance = batsman.running * bowler.bowling * self.field.pitch_conditions
        if lbw_chance > lbw_threshold:
            return "LBW"
        return "NOT OUT"

    def handle_catch(self, batsman, fielder):
        # Implement logic to handle catches
        catch_threshold = 0.8  # Adjust this threshold as needed
        catch_chance = batsman.batting * fielder.fielding * self.field.pitch_conditions
        if catch_chance > catch_threshold:
            return "CAUGHT"
        return "NOT OUT"

    def handle_no_ball(self):
        # Implement logic to handle no-balls
        no_ball_chance = 0.1  # Adjust this chance as needed
        if random.random() < no_ball_chance:
            return True
        return False

    def handle_wide_ball(self):
        # Implement logic to handle wide-balls
        wide_ball_chance = 0.1  # Adjust this chance as needed
        if random.random() < wide_ball_chance:
            return True
        return False


# In[5]:


class Commentator:
    def __init__(self, umpire):
        """
        Initialize a Commentator object with the provided attributes.
        
        Args:
            umpire (Umpire): The Umpire object providing match information.
        """
        self.umpire = umpire

    def describe_ball(self, batsman, bowler):
        """
        Generate a description of the ball played by the batsman.
        
        Args:
            batsman (Player): The Player object representing the batsman.
            bowler (Player): The Player object representing the bowler.
        
        Returns:
            str: The description of the ball played by the batsman.
        """
        outcome = self.umpire.predict_outcome(batsman, bowler)
        print("Outcome: ", outcome)
        if outcome == "OUT":
            description = f"{batsman.name} is OUT!"
        else:
            description = f"{batsman.name} plays the shot."

        return description
    def describe_game(self, captain1, captain2, country1, country2, over):
        """
        Provide a description of the cricket match.
        
        Args:
            captain1 (str): The name of the captain of the first team.
            captain2 (str): The name of the captain of the second team.
            country1 (str): The name of the first team.
            country2 (str): The name of the second team.
            over (int): The total number of overs in the match.
        """
        print("\n--------- Game Information ---------\n")
        print(f"{country1} Vs {country2}")
        print(f"Captain 1 : {captain1}, Captain 2 : {captain2}")
        print(f"Over : {over}")
        print("\n---------------------------------------------\n")

    def describe_start(self, team):
        """
        Provide a description of the start of an innings.
        
        Args:
            team (str): The name of the team currently batting.
        """
        print("\n------------- GAME STARTED ------------------\n")
        print(f"Team {team} playing: ")
    
    def describe_end(self):
        """
        Provide a description of the end of an innings.
        """
        print(f"\n\nFinal Run: {self.umpire.scores} Wicket: {self.umpire.wickets} Overs: {self.umpire.overs}")
        print("\n---------------------------------------------\n")

    
    def current_info(self, ball_count):
        """
        Provide the current match information.
        
        Args:
            ball_count (int): The count of balls played in the current over.
        """
        print(f"Balls: {ball_count} Over: {self.umpire.overs} Run: {self.umpire.scores}  Wicket: {self.umpire.wickets}")

    def describe_final_result(self, name, scores):
        """
        Provide a description of the final result of the match.
        
        Args:
            name (str): The name of the winning team.
            scores (int): The```
            score achieved by the winning team.
        """
        print("--------------- Winner -----------------------")
        print(f"TEAM : {name} IS THe WINNER OF THE TOURNAMENT :")
        print("\n---------------------------------------------\n")
    


# In[9]:


class Match:
    def __init__(self, team1, team2, team3, team4, field, total_overs):
        """
        Represents a cricket match between two teams.
        
        Args:
            team1 (Team): The Team object representing the first team.
            team2 (Team): The Team object representing the second team.
            team3 (Team): The Team object representing the third team.
            team4 (Team): The Team object representing the fourth team.
            field (Field): The Field object representing the field conditions.
            total_overs (int): The total number of overs in each match.
        """
        self.team1 = team1
        self.team2 = team2
        self.team3 = team3
        self.team4 = team4
        self.field = field
        self.total_overs = total_overs
        self.final_winner = None  # To store the winner of the final match
        self.umpire = Umpire(field)  # Instantiate an Umpire object
        self.commentator = Commentator(self.umpire)  # Pass the umpire to the Commentator constructor
    def print_trophy(self):
        trophy = """
        ╭───────────────────╮
        │                   │
        │    CONGRATULATIONS!    │
        │                   │
        │      ___________      │
        │     '._==_==_=_.'     │
        │     .-\\:      /-.    │
        │    | (|:.     |) |    │
        │     '-|:.     |-'     │
        │       \\::.    /      │
        │        '::. .'        │
        │          ) (          │
        │        _.' '._        │
        │       `'''''''`       │
        ╰───────────────────╯
        """
        print(trophy)

    def start_tournament(self):
        # Simulate the entire tournament
        print("\n--------- Tournament Started ---------\n")

        # Qualification round
        print("\n----- Qualification Round -----\n")
        final_teams = self.simulate_qualification_round()

        # Final match
        print("\n----- Final Match -----\n")
        tournament_winner = self.simulate_final_match(final_teams[0], final_teams[1])

        # Declare the tournament winner
        self.commentator.describe_final_result(tournament_winner.name, tournament_winner.captain.name)
        self.print_trophy()
        print("\n--------- Tournament Ended ---------\n")
    
    def simulate_qualification_round(self):
        # Simulate matches between team1 and team2, and team3 and team4
        match1_winner = self.simulate_individual_match(self.team1, self.team2)
        match2_winner = self.simulate_individual_match(self.team3, self.team4)
        
        return [match1_winner, match2_winner]

    def simulate_final_match(self, team1, team2):
        # Simulate the final match between the qualified teams
        final_match = self.simulate_individual_match(team1, team2)
        self.final_winner = final_match
        return self.final_winner

    
    def play_innings(self, batting_team, bowling_team):
        """
        Simulates the innings of a team.

        Args:
            batting_team (Team): The Team object representing the batting team.
            bowling_team (Team): The Team object representing the bowling team.
        """
        ball_count = 1
        over = 0
        bowler = bowling_team.choose_bowler()
        batsman = batting_team.sending_next_player()

        while over < self.total_overs:
            print("\n")
            self.commentator.current_info(ball_count)
            ball_description = self.commentator.describe_ball(batsman, bowler)

            print(ball_description)
            if ball_description.endswith("OUT!"):
                batsman = batting_team.sending_next_player()
                if batsman is None:
                    break
                self.umpire.update_wickets()
                print(f"Wickets: {self.umpire.wickets} , Overs: {self.umpire.overs}")
                print(f"New player {batsman.name} is playing...")
            else:
                runs = random.randint(0, 6)
                self.umpire.update_score(runs)

            if ball_count > 5:
                over += 1
                print(f"Over {over} Starting...")
                self.umpire.update_overs()
                bowler = bowling_team.choose_bowler()
                ball_count = 0

            self.commentator.current_info(ball_count)
            ball_count += 1

    def simulate_individual_match(self, team1, team2):
        # Simulate an individual match between two teams
        team1.select_captain(random.choice(team1.players))
        team2.select_captain(random.choice(team2.players))
        team1.batting_order = team1.players.copy()
        team2.batting_order = team2.players.copy()
        team1.bowlers = team1.players.copy()
        team2.bowlers = team2.players.copy()

        self.commentator.describe_game(
            team1.captain.name, team2.captain.name, team1.name, team2.name, over=self.total_overs
        )

        # Team 1 playing
        self.commentator.describe_start(team1.name)
        self.play_innings(team1, team2)
        self.commentator.describe_end()
        lastScores = self.commentator.umpire.scores

        # Team 2 playing
        self.commentator.umpire.scores = 0
        self.commentator.umpire.wickets = 0
        self.commentator.umpire.overs = 0
        self.commentator.describe_start(team2.name)
        self.play_innings(team2, team1)
        self.commentator.describe_end()
        newScores = self.commentator.umpire.scores

        if lastScores > newScores:
            return team1
        else:
            return team2
    


# In[10]:


# Creating fake data
# Adding the players
indian_player_names = ["Virat Kohli", "Rohit Sharma", "Jasprit Bumrah", "Ravindra Jadeja", "Shikhar Dhawan", "KL Rahul", "Hardik Pandya", "Yuzvendra Chahal", "Bhuvneshwar Kumar", "Mohammed Shami"]
england_player_names = ["Joe Root", "Ben Stokes", "Jofra Archer", "Jos Buttler", "Jonny Bairstow", "Eoin Morgan", "Chris Woakes", "Mark Wood", "Adil Rashid", "Sam Curran"]
australia_player_names = ["Steve Smith", "David Warner", "Pat Cummins", "Glenn Maxwell", "Mitchell Starc", "Aaron Finch", "Adam Zampa", "Matthew Wade", "Josh Hazlewood", "Alex Carey"]
pakistan_player_names = ["Babar Azam", "Shaheen Afridi", "Shadab Khan", "Fakhar Zaman", "Mohammad Rizwan", "Imad Wasim", "Hassan Ali", "Sarfaraz Ahmed", "Wahab Riaz", "Haris Rauf"]
# Adding players to the respective teams

team1 = Team("India", [Player(name, round(random.random(), 1), round(random.random(), 1), round(random.random(), 1), round(random.random(), 1), round(random.random(), 1)) for name in indian_player_names])
team2 = Team("England", [Player(name, round(random.random(), 1), round(random.random(), 1), round(random.random(), 1), round(random.random(), 1), round(random.random(), 1)) for name in england_player_names])
team3 = Team("Australia", [Player(name, round(random.random(), 1), round(random.random(), 1), round(random.random(), 1), round(random.random(), 1), round(random.random(), 1)) for name in australia_player_names])
team4 = Team("Pakistan", [Player(name, round(random.random(), 1), round(random.random(), 1), round(random.random(), 1), round(random.random(), 1), round(random.random(), 1)) for name in pakistan_player_names])
# Adding players to team


# showing the field
field = Field("Large", 0.7, 0.8, 0.9)

# starting match simulation
total_overs = 5
tournament = Match(team1, team2, team3, team4, field, total_overs)
tournament.start_tournament()


# In[ ]:





# In[ ]:




