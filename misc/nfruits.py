def eatandbuy(fruits, fruit_id):
    """
    :param fruits: a non-empty dictionary containing type of fruit and its quantity
    :param fruit_id: string with length of 1, containing id of fruit
    :return: modified dictionary containing type of fruit and its quantity
    """
    if fruit_id not in fruits:
        raise ValueError("There is no such fruit" + fruit_id)
    if fruits[fruit_id] < 1:
        raise ValueError("Unable to eat specified fruit " + fruit_id)

    print "Eating fruit " + fruit_id
    #substract 2 from fruits we're eating; then add one fruit of each type
    fruits[fruit_id] -= 2
    for fruit in fruits:
        fruits[fruit] += 1
    return fruits


def nfruits(fruits, pattern):
    """
    Function takes the following arguments:
    - fruits; A non-empty dictionary containing type of fruit and its quantity initially with Python when he leaves home (length < 10)
    - pattern: A string pattern of the fruits eaten by Python on his journey as observed by Cobra.

    Function returns the maximum quantity out of the different types of fruits that is available with Python when he has reached the campus.
    """
    assert len(fruits) > 0, "List of fruits is empty"
    assert len(fruits) < 10, "Too many fruits in list"

    for letter in pattern[:-1]:
        fruits = eatandbuy(fruits, letter, )
        print fruits

    # eating last fruit
    assert fruits[pattern[-1]] > 0, "Unable to eat specified fruit " + pattern[-1]
    fruits[pattern[-1]] -= 1

    return fruits[max(fruits, key=fruits.get)]  # return result



print nfruits({'C': 9, 'K': 5, 'L': 6, 'N': 9, 'Q': 9, 'V': 8, 'X': 8}, 'LK')