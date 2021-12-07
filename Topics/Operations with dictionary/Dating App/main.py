def select_dates(potential_dates):
    match = []
    for date in potential_dates:
        if date['age'] > 30 and 'art' in date['hobbies'] and date['city'] == 'Berlin':
            match.append(date['name'])
    return ', '.join(match)
