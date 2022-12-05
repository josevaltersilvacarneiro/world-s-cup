"""The functions of this file are responsible
for registering the teams and the games.

"""

from _utils import (
            get_amount,
            get_group,
            get_team, get_two_different_teams,
            get_date, get_place,
            number_of_teams_registered, number_of_games_registered,
        );

def _register_team(cup : dict) -> None:

    groups : list = cup.keys();

    while cup[( group := get_group(groups) )].__len__() > 3:
        print(f'The group {group} is already complete');

    team = get_team(cup, group);

    cup[group].append(team);

def _register_game(cup : dict, games : dict) -> None:

    groups : list = cup.keys();

    while True:

        group : str = get_group(groups);

        if games[group].__len__() == 6:
            print('All games in this group already were registered');
        if games[group].__len__() == _max_number_of_games_registered_in_the_group(cup, group):
            print('To register more games in this group, add more teams!');
        else:
            break;

    first_team, second_team = get_two_different_teams(cup, group, False);

    num_of_goals_team_one : int = get_amount(f'Number of goals for {first_team}: ');
    num_of_goals_team_two : int = get_amount(f'Number of goals for {second_team}: ');

    time = get_date();

    game = [
            first_team,
            second_team,
            num_of_goals_team_one,
            num_of_goals_team_two,
            f'{time[0]}:{time[1]}, {time[2]}/{time[3]}',
            get_place(),
        ];

    games[group].append(game);

def _number_of_teams_to_register(cup : dict) -> int:
    
    return 8 * 4 - number_of_teams_registered(cup);

def _max_number_of_games_registered_in_the_group(cup : dict, group : str) -> int:

    # Fundamental Counting Theorem

    num_of_teams_registered_in_the_group : int = len(cup[group]);
    num_of_possible_games = num_of_teams_registered_in_the_group * (num_of_teams_registered_in_the_group - 1) / 2;

    return num_of_possible_games;

def _max_number_of_games_registered(cup : dict) -> int:
    """Using a repetiton loop, all groups looped.
    By means of The Fundamental Counting Theorem,
    the number of possible games in each group is
    found and then added to the accumulator varia-
    ble called 'max_sum_of_games_registered'. At
    the end, it's returned.

    """

    max_num_of_games_registered : int = 0;

    for group in cup.keys():
        max_num_of_games_registered += _max_number_of_games_registered_in_the_group(cup, group);

    return max_num_of_games_registered;

def _number_of_games_to_register(cup : dict, games : dict) -> int:
    
    return _max_number_of_games_registered(cup) - number_of_games_registered(games);

#--------------------------------------------------------------------------------------#
######################################### public #######################################

def register_teams(cup : dict) -> None:
    
    max_amount : int = _number_of_teams_to_register(cup);

    while ( amount_of_teams := get_amount('Number of teams: ') ) > max_amount:
        print(f'Only {max_amount} teams left to register');

    for i in range(amount_of_teams):
        _register_team(cup);

def register_games(cup : dict, games : dict) -> None:
    
    max_amount : int = _number_of_games_to_register(cup, games);

    while ( amount_of_games := get_amount('Number of games: ') ) > max_amount:
        print(f'Only {max_amount} games left to register');
    
    for i in range(amount_of_games):
        _register_game(cup, games);

