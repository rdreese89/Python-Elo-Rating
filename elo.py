from math import pow
import csv

def expected_outcome(player_a_elo: float, player_b_elo: float) -> float:
    """
    Calculates the expected outcome of a match between two players based on their ELO ratings.
    The output is a value between 0 and 1, representing the probability of player A winning the match.

    Args:
    player_a_elo (float): the ELO rating of player A
    player_b_elo (float): the ELO rating of player B

    Returns:
    float: the expected outcome of a match between player A and player B
    """
    return 1 / (1 + pow(10, (player_b_elo - player_a_elo) / 400))


def update_elo(player_a_elo: float, player_b_elo: float, result: float, k_factor: int = 32) -> tuple:
    """
    Updates the ELO ratings of two players based on the result of their match and a chosen K-factor.

    Args:
    player_a_elo (float): the initial ELO rating of player A
    player_b_elo (float): the initial ELO rating of player B
    result (float): the result of the match (0 for a loss, 0.5 for a draw, or 1 for a win)
    k_factor (int, optional): the K-factor to use for the update calculation (default is 32)

    Returns:
    tuple: the updated ELO ratings of player A and player B
    """
    expected_a = expected_outcome(player_a_elo, player_b_elo)
    expected_b = 1 - expected_a
    actual_a = result
    actual_b = 1 - result
    new_a_elo = player_a_elo + k_factor * (actual_a - expected_a)
    new_b_elo = player_b_elo + k_factor * (actual_b - expected_b)
    return (new_a_elo, new_b_elo)


def elo_rating(player_a_elo: float, player_b_elo: float, result: float, k_factor: int = 32) -> tuple:
    """
    Combines the expected_outcome() and update_elo() functions to calculate the updated ELO ratings of two players.

    Args:
    player_a_elo (float): the initial ELO rating of player A
    player_b_elo (float): the initial ELO rating of player B
    result (float): the result of the match (0 for a loss, 0.5 for a draw, or 1 for a win)
    k_factor (int, optional): the K-factor to use for the update calculation (default is 32)

    Returns:
    tuple: the updated ELO ratings of player A and player B
    """
    return update_elo(player_a_elo, player_b_elo, result, k_factor)

def set_ratings(df) -> dict:
    """
    Combines the unique values in the 'Fighter' and 'Opponent' columns of the data frame.
    It then returns a dictionary with each element of the list paired with a value of '1500'.

    Args:
    df: the Pandas dataframe containing fight records

    Returns:
    dictionary: the dictionary of unique fighters with default ratings
    """
    list1 = list(df['Fighter'].unique())
    list2 = list(df['Opponent'].unique())
    players = list1 + list2
    players = list(dict.fromkeys(players))
    player_ratings = dict.fromkeys(players,1500) 
    return player_ratings

def write_dict_to_csv(dict, filename) -> None:
    """
    Writes a dictionary to a two-column CSV file.

    Parameters:
    dict_data (dict): A dictionary to write to a CSV file. The keys will be written to the first column, and the values will be written to the second column.
    filename (str): The name of the file to write the CSV data to.

    Returns: 
    None.
    """
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in dict.items():
                writer.writerow([key, value])
    except Exception as e:
        print(f"An error occurred while writing to CSV: {e}")

