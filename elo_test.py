import elo as elo
import pandas as pd


df = pd.read_csv('cleaned_data.csv')

df['W/L'] = df['W/L'].map({'W':1,'L':0,'D':0.5})

player_ratings = elo.set_ratings(df)

for index, row in df.iterrows():
    fighter = row['Fighter']
    opponent = row['Opponent']
    win = row['W/L']

    print(str(fighter) + " vs " + str(opponent) + " - " + "Result: " + str(win))

    fighter_elo = player_ratings.get(fighter, 1500)
    opponent_elo = player_ratings.get(opponent, 1500)

    new_elo = elo.elo_rating(fighter_elo, opponent_elo, win)

    player_ratings.update({fighter: new_elo[0]})
    player_ratings.update({opponent: new_elo[1]})

    print(str(fighter) + "'s new rating: " + str(player_ratings[fighter]))
    print(str(opponent) + "'s new rating: " + str(player_ratings[opponent]))

elo.write_dict_to_csv(player_ratings, "rankings.csv")
