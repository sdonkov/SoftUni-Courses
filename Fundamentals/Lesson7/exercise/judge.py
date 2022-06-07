def add_user():
    if contest not in contests_dict:
        contests_dict[contest] = {}
    if username not in contests_dict[contest]:
        contests_dict[contest][username] = points
        if username not in individual_statistics:
            individual_statistics[username] = points
        else:
            individual_statistics[username] += points
    else:
        if points > contests_dict[contest][username]:
            individual_statistics[username] -= contests_dict[contest][username]
            individual_statistics[username] += points
            contests_dict[contest][username] = points


def repr():
    for contest in contests_dict:
        print(f'{contest}: {len(contests_dict[contest])} participants')
        sorted_by_name = {key: value for key, value in sorted(contests_dict[contest].items())}
        sorted_by_value = {key: value for key, value in
                           sorted(sorted_by_name.items(), key=lambda item: item[1], reverse=True)}
        n = 0
        for username, points in sorted_by_value.items():
            n += 1
            print(f'{n}. {username} <::> {points}')

    individual_statistics_by_name = {key: value for key, value in sorted(individual_statistics.items())}
    individual_statistics_by_points = {key: value for key, value in
                                       sorted(individual_statistics_by_name.items(), key=lambda item: item[1],
                                              reverse=True)}
    print('Individual standings:')
    n = 0
    for username, points in individual_statistics_by_points.items():
        n += 1
        print(f'{n}. {username} -> {points}')


contests_dict = {}
individual_statistics = {}

while True:
    data = input()
    if data == 'no more time':
        break
    username, contest, points = data.split(' -> ')
    points = int(points)
    add_user()

repr()