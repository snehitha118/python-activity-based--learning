
print("SPORTS TOURNAMENT RANKING SYSTEM")
print("-----------------------------------")

try:
    n = int(input("Enter number of teams: "))

    if n < 2:
        print("Invalid input! At least 2 teams are required.")

    else:
        teams = {}

       
        for i in range(n):
            name = input("Enter team name " + str(i + 1) + ": ").strip()

            if not name or name in teams:
                raise ValueError("Team names must be unique and non-empty.")

            teams[name] = {
                "MP": 0,
                "W": 0,
                "D": 0,
                "L": 0,
                "GF": 0,
                "GA": 0,
                "Points": 0
            }

        matches = int(input("\nEnter number of matches: "))

        if matches < 0:
            raise ValueError("Number of matches cannot be negative.")

        # Store match results
        for i in range(matches):
            print("\nMatch", i + 1)

            team1 = input("Enter first team: ").strip()
            team2 = input("Enter second team: ").strip()

            if (team1 not in teams or team2 not in teams
                    or team1 == team2):
                raise ValueError("Invalid team names.")

            score1 = int(input("Enter " + team1 + " score: "))
            score2 = int(input("Enter " + team2 + " score: "))

            if score1 < 0 or score2 < 0:
                raise ValueError("Scores cannot be negative.")

          
            teams[team1]["MP"] += 1
            teams[team2]["MP"] += 1

            teams[team1]["GF"] += score1
            teams[team1]["GA"] += score2

            teams[team2]["GF"] += score2
            teams[team2]["GA"] += score1

            
            if score1 > score2:
                teams[team1]["W"] += 1
                teams[team1]["Points"] += 3
                teams[team2]["L"] += 1

            elif score2 > score1:
                teams[team2]["W"] += 1
                teams[team2]["Points"] += 3
                teams[team1]["L"] += 1

            else:
                teams[team1]["D"] += 1
                teams[team2]["D"] += 1
                teams[team1]["Points"] += 1
                teams[team2]["Points"] += 1

       
        for name in teams:
            teams[name]["GD"] = (
                teams[name]["GF"] - teams[name]["GA"]
            )

        
        ranking = sorted(
            teams.items(),
            key=lambda item: (
                item[1]["Points"],
                item[1]["GD"],
                item[1]["GF"]
            ),
            reverse=True
        )

      
        print("\nSPORTS TOURNAMENT FINAL RANKINGS")
        print("-" * 78)

        print(
            f"{'Rank':<6}{'Team':<15}{'MP':<5}"
            f"{'W':<5}{'D':<5}{'L':<5}"
            f"{'GF':<6}{'GA':<6}{'GD':<6}{'Points':<8}"
        )

        print("-" * 78)

        for rank, (name, stats) in enumerate(ranking, 1):
            print(
                f"{rank:<6}{name:<15}{stats['MP']:<5}"
                f"{stats['W']:<5}{stats['D']:<5}"
                f"{stats['L']:<5}{stats['GF']:<6}"
                f"{stats['GA']:<6}{stats['GD']:<6}"
                f"{stats['Points']:<8}"
            )

        print("-" * 78)

        print("\nWinner:", ranking[0][0])
        print("\nThank you!")

except ValueError as e:
    print("\nInvalid input:", e)

