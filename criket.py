import random
import time

# Game constants
no_runs_required = -1
unlimited_overs = -1
all_out_wickets = 10
balls = ["0", "1", "2", "3", "4", "6", "Owzthat!"]
decisions = ["Not Out!", "Bowled!", "Caught!", "LBW!", "Run Out!", "Stumped!", "Not Out!"]
game_rate = 0.25  # seconds between balls
overs_per_team = 6
team1 = "India"
team2 = "England"

# Get user input for field type and field size
field_type = input("Enter field type (dry/wet): ")
field_size = input("Enter field size (large/medium/small): ")

class Field:
    def return_to_mark(self):
        """Simulate the time taken for the bowler to return to their mark."""
        time.sleep(game_rate)
        
    def __init__(self, field_type, field_size):
        self.field_type = field_type
        self.field_size = field_size

class Umpire:
    def __init__(self):
        self.teams = [team1, team2]
        
    def make_decision(self):
        """Simulate the time taken for the umpire to make a decision."""
        time.sleep(game_rate * 2)
        
    def roll_dice(self, dice_type):
        """Roll a dice to simulate bowl or decision."""
        if dice_type == "bowl":
            return balls[random.randint(0, len(balls) - 1)]
        elif dice_type == "decision":
            self.make_decision()
            return decisions[random.randint(0, len(decisions) - 1)]
        else:
            return "0"
    
    def toss(self):
        """Toss a coin to decide which team chooses to bat or bowl."""
        toss_result = random.choice([team1, team2])
        decision = random.choice(["bat", "bowl"])
        
        if decision == "bat":
            batting_team = toss_result
            bowling_team = team2 if toss_result == team1 else team1
        else:
            bowling_team = toss_result
            batting_team = team2 if toss_result == team1 else team1
        
        return f"{toss_result} wins the toss and chooses to {decision}", batting_team, bowling_team

class Commentator:
    def display_event(self, event, batting_team, score, wickets, overs, balls):
        """Display commentary for the event."""
        unfinished_over_balls = balls % 6
        overs_completed = balls // 6
        print("{} - {} {}/{} ({}.{} overs)".format(event, batting_team, score, wickets, overs_completed, unfinished_over_balls))

class Match:
    def __init__(self, field_type, field_size):
        self.field = Field(field_type, field_size)
        self.umpire = Umpire()
        self.commentator = Commentator()
    def innings(self, batting_team, max_overs, runs_required):
        """Simulate a single innings."""
        wickets = 0
        score = 0
        bowled = 0
        overs = 0

        while wickets < all_out_wickets and \
              (not score > runs_required or runs_required == no_runs_required) and \
              (overs < max_overs or max_overs == unlimited_overs):
            ball = self.umpire.roll_dice("bowl")
            event = ""
            if ball == "Owzthat!":
                decision = self.umpire.roll_dice("decision")
                event = decision
                if decision != "Not Out!":
                    wickets += 1
            else:
                event = "{} run".format(ball)
                if ball != "1":
                    event += "s"
                score += int(ball)
            
            # Adjust the run scoring based on field conditions
            if self.field.field_type == "wet" or self.field.field_size == "large":
                score -= 1  # Reduced run scoring

            bowled += 1
            self.commentator.display_event(event, batting_team, score, wickets, overs, bowled)

            self.field.return_to_mark()
            overs = bowled // 6

        return {"Runs": score, "Wickets": wickets, "Overs": overs, "Balls": bowled}

    def run_match(self):
        # Toss and display results
        toss_result, batting_team, bowling_team = self.umpire.toss()
        print("Toss Result: {}".format(toss_result))
        
        # Rest of the match logic remains unchanged
        first_innings = self.innings(batting_team, overs_per_team, no_runs_required)
        print("{} score {}/{} in {}.{} overs".format(batting_team, first_innings["Runs"], first_innings["Wickets"], first_innings["Overs"], first_innings["Balls"]))
        second_innings = self.innings(bowling_team, overs_per_team, first_innings["Runs"])
        print("{} score {}/{} in {}.{} overs".format(bowling_team, second_innings["Runs"], second_innings["Wickets"], second_innings["Overs"], second_innings["Balls"]))

        if first_innings["Runs"] > second_innings["Runs"]:
            print("{} win by {} runs!".format(batting_team, first_innings["Runs"] - second_innings["Runs"]))
        elif first_innings["Runs"] < second_innings["Runs"]:
            print("{} win by {} wickets!".format(bowling_team, 10 - second_innings["Wickets"]))
        else:
            print("Tied game!")



if __name__ == "__main__":
    cricket_match = Match(field_type, field_size)
    cricket_match.run_match()
