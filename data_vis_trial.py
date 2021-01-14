highest_reviewed_per_year = {{'Author': 'Sarah Young',
        'Genre': 'Non Fiction',
        'Name': 'Jesus Calling: Enjoying Peace in His Presence (with Scripture '
                'References)',
        'Price': 8,
        'Reviews': 19576,
        'User Rating': 4.9,
        'Year': 2011}, {'Author': 'Dr. Seuss',
        'Genre': 'Fiction',
        'Name': "Oh, the Places You'll Go!",
        'Price': 8,
        'Reviews': 21834,
        'User Rating': 4.9,
        'Year': 2012}}
 

y = []
for item in highest_reviewed_per_year:
    if highest_reviewed_per_year.get(item["Reviews"]):
        y.append(item["Reviews"])

print(y)

# cannot hash dictionary to a list

