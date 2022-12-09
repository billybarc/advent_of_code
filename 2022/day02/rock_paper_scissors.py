# A = Rock, B = Paper, C = Scissors
# X = Rock, Y = Paper, Z = Scissors

with open("input.txt") as f:
    dat = f.read()

# list of games where a game is a list
# of player actions
game_list = [x.split(' ') for x in dat.splitlines()]

# value of each action
score_dict = {"X": 1, "Y": 2, "Z": 3}

# dict of dicts to find p2 score. Each inner
# dict contains the scores for p1's action
# based on the p2 action that selected the inner
# dict
scores_a2_a1 = {"X": {"A": 3, "B": 0, "C": 6},
                "Y": {"A": 6, "B": 3, "C": 0},
                "Z": {"A": 0, "B": 6, "C": 3}}

def get_p2_outcome_points(a1, a2):
    return scores_a2_a1[a2][a1]

points_from_action = [score_dict[x[1]] for x in game_list]
points_from_outcome = [get_p2_outcome_points(x[0], x[1]) for x in game_list]
points_per_game = points_from_action + points_from_outcome
total_points = sum(points_per_game)
print(f"Player 2's total score is {total_points}.")


# part 2
# now X means lose, Y means draw, Z means win
# so now we must calculate the proper p2 action
# to get outcome from the strategy guide.
# Then apply same scoring process

a1_list = ["A", "B", "C"]
a2_list = ["X", "Y", "Z"]

# with one-based indexing, losing response is
# (idx + 1) % 3 + 1,
# winning response is
# idx % 3 + 1
# To convert to pythonic indices,
# need to add 1 to indices from index() lookup
# and subtract 1 on the way out to get back to python
# indices

def get_p2_response_by_strat(a1, strat):
    match strat:
        case "X":
            return a2_list[(a1_list.index(a1) + 1 + 1) % 3]
        case "Y":
            return a2_list[a1_list.index(a1)]
        case "Z":
            return a2_list[(a1_list.index(a1) + 1) % 3]

p2_responses = [get_p2_response_by_strat(x[0], x[1]) for x in game_list]
points_from_action = [score_dict[x] for x in p2_responses]
points_from_outcome = [get_p2_outcome_points(x[0], y) for (x, y) in zip(game_list, p2_responses)]
points_per_game = points_from_action + points_from_outcome
total_points = sum(points_per_game)
print(f"Player 2's total score is {total_points}.")
