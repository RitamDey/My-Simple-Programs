def manhattan(rating1, rating2):
    """
    Computes the Manhattan distance. Both rating1 and rating2 are
    dictionaries of the form
    {'The Strokes': 3.0, 'Slightly Stoopid': 2.5 ...
    """

    distance = 0
    for rating in rating1:  # Get each band name
        if rating in rating2:  # If the band is in the second ratings
            distance += abs(rating1[rating] - rating2[rating])
    return distance


def minikowski(rating1, rating2, users_count):
    """
    Computes the Manhattan distance. Both rating1 and rating2 are
    dictionaries of the form
    {'The Strokes': 3.0, 'Slightly Stoopid': 2.5 ...
    """

    distance = 0
    for rating in rating1:  # Get each band name
        if rating in rating2:  # If the band is in the second ratings
            distance += abs(rating1[rating] - rating2[rating])**users_count
    return distance**1 / users_count


def computeNearestNeighbor(username, users):
    """
    Creates a sorted list of users based on their distance to
    username
    """

    distances = []
    for user in users:  # Get all the user name from the passed dict
        if user != username:
            # Get the distance based on ratings
            # manhattan(users[user], users[username]),
            distance = minikowski(user[user], users[username], 2)
            distances.append((distance, user))

    # sort based on distance -- closet first
    distances.sort()
    return distances


def recommend(username, users):
    # Get the name of the nearest neighbour
    nearest = computeNearestNeighbor(username, users)[0][1]
    recommendations = []

    # now find bands neighbor rated that user didn't
    neighborRatings = users[nearest]
    userRatings = users[username]
    for artist in neighborRatings:
        if artist not in userRatings:
            recommendations.append((artist, neighborRatings[artist]))

    # using the fn sorted for variety - sort is more efficient
    # sort using the ratings
    return sorted(recommendations,
                  key=lambda artistTuple: artistTuple[1],
                  reverse=True)


if __name__ == "__main__":
    users = {
        "Angelica": {
            "Blues Traveler": 3.5, "Broken Bells": 2.0,
            "Norah Jones": 4.5, "Phoenix": 5.0,
            "Slightly Stoopid": 1.5,
            "The Strokes": 2.5, "Vampire Weekend": 2.0
        },
        "Bill": {
            "Blues Traveler": 2.0, "Broken Bells": 3.5,
            "Deadmau5": 4.0, "Phoenix": 2.0,
            "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0
        },
        "Chan": {
            "Blues Traveler": 5.0, "Broken Bells": 1.0,
            "Deadmau5": 1.0, "Norah Jones": 3.0,
            "Phoenix": 5, "Slightly Stoopid": 1.0
        },
        "Dan": {
            "Blues Traveler": 3.0, "Broken Bells": 4.0,
            "Deadmau5": 4.5, "Phoenix": 3.0,
            "Slightly Stoopid": 4.5, "The Strokes": 4.0,
            "Vampire Weekend": 2.0
        },
        "Hailey": {
            "Broken Bells": 4.0, "Deadmau5": 1.0,
            "Norah Jones": 4.0, "The Strokes": 4.0,
            "Vampire Weekend": 1.0
        },
        "Jordyn": {
            "Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0,
            "Phoenix": 5.0, "Slightly Stoopid": 4.5,
            "The Strokes": 4.0, "Vampire Weekend": 4.0
        },
        "Sam": {
            "Blues Traveler": 5.0, "Broken Bells": 2.0,
            "Norah Jones": 3.0, "Phoenix": 5.0,
            "Slightly Stoopid": 4.0, "The Strokes": 5.0
        },
        "Veronica": {
            "Blues Traveler": 3.0, "Norah Jones": 5.0,
            "Phoenix": 4.0, "Slightly Stoopid": 2.5,
            "The Strokes": 3.0
        }
    }


print(recommend('Angelica', users))
