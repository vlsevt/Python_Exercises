"""EX05 - Hobbies."""
import collections
import fractions
import itertools


def create_dictionary(data: str) -> dict:
    """
    Create dictionary about people and their hobbies ie. {name1: [hobby1, hobby2, ...], name2: [...]}.

    There should be no duplicate hobbies on 1 person.

    :param data: given string from database
    :return: dictionary where keys are people and values are lists of hobbies
    """
    names_and_hobbies = {}
    for i in data.split("\n"):
        name = i[0:i.index(":")]
        hobby = f"{i[i.index(':') + 1 :-1]}{i[-1]}"
        if name not in names_and_hobbies:
            names_and_hobbies[name] = list()
            names_and_hobbies[name].append(hobby)
        elif name in names_and_hobbies:
            if hobby not in names_and_hobbies[name]:
                names_and_hobbies[name].append(hobby)
    return names_and_hobbies


def sort_dictionary(dic: dict) -> dict:
    """
    Sort dictionary values alphabetically.

    The order of keys is not important.

    sort_dictionary({"b":[], "a":[], "c": []})  => {"b":[], "a":[], "c": []}
    sort_dictionary({"": ["a", "f", "d"]})  => {"": ["a", "d", "f"]}
    sort_dictionary({"b":["d", "a"], "a":["c", "f"]})  => {"b":["a", "d"], "a":["c", "f"]}
    sort_dictionary({"Jack": ["swimming", "hiking"], "Charlie": ["games", "yoga"]})
        => {"Jack": ["hiking", "swimming"], "Charlie": ["games", "yoga"]}

    :param dic: dictionary to sort
    :return: sorted dictionary
    """
    for i in dic:
        dic[i] = sorted(dic[i])
    return dic


def create_dictionary_with_hobbies(data: str) -> dict:
    """
    Create dictionary about hobbies and their hobbyists ie. {hobby1: [name1, name2, ...], hobby2: [...]}.

    :param data: given string from database
    :return: dictionary, where keys are hobbies and values are lists of people. Values are sorted alphabetically
    """
    new_data = data.split("\n")
    names_and_hobbies = {}
    for i in new_data:
        name = i[0:i.index(":")]
        hobby = f"{i[i.index(':') + 1 :-1]}{i[-1]}"
        if hobby not in names_and_hobbies:
            names_and_hobbies[hobby] = list()
            names_and_hobbies[hobby].append(name)
        elif hobby in names_and_hobbies:
            if name not in names_and_hobbies[hobby]:
                names_and_hobbies[hobby].append(name)
    return sort_dictionary(names_and_hobbies)


def find_people_with_most_hobbies(data: str) -> list:
    """
    Find the people who have the most hobbies.

    :param data: given string from database
    :return: list of people with most hobbies. Sorted alphabetically.
    """
    names = []
    length = 0
    dic = create_dictionary(data)
    for i in dic:
        if len(dic[i]) > length:
            length = len(dic[i])
    for i in dic:
        if len(dic[i]) == length:
            names.append(i)
    return sorted(names)


def find_least_popular_hobbies(data: str) -> list:
    """
    Find the least popular hobbies.

    :param data: given string from database
    :return: list of least popular hobbies. Sorted alphabetically.
    """
    hobbies = []
    length = 9223372036854775807
    dic = create_dictionary_with_hobbies(data)
    for i in dic:
        if len(dic[i]) < length:
            length = len(dic[i])
    for i in dic:
        if len(dic[i]) == length:
            hobbies.append(i)
    return sorted(hobbies)


def sort_names_and_hobbies(data: str) -> tuple:
    """
    Create a tuple of sorted names and their hobbies.

    The structure of the tuple is as follows:
    (
        (name1, (hobby1, hobby2)),
        (name2, (hobby1, hobby2)),
         ...
    )

    For each person, there is a tuple, where the first element is the name (string)
    and the second element is an ordered tuple of hobbies (ordered alphabetically).
    All those person-tuples are ordered by the name of the person and are inside a tuple.
    """
    dic = sort_dictionary((create_dictionary(data)))
    dic1 = sorted(dic)
    sorted_dict = {key: dic[key] for key in dic1}
    new_dic = ()
    hobbies = ()
    for i in sorted_dict:
        for hobby in sorted_dict[i]:
            hobbies = hobbies + (hobby,)
        new_dic = new_dic + ((i, hobbies),)
        hobbies = ()
    return new_dic


def find_people_with_hobbies(data: str, hobbies: list) -> set:
    r"""
    Find all the different people with certain hobbies.

    It is recommended to use set here.

    Example:
        data="John:running\nMary:running\nJohn:dancing\nJack:dancing\nJack:painting\nSmith:painting"
        hobbies=["running", "dancing"]
    Result:
        {"John", "Mary", "Jack"}
    """
    dic = create_dictionary(data)
    names = set()
    for i in dic:
        for hobby in dic[i]:
            if hobby in hobbies:
                names.add(i)
    return names


def find_two_people_with_most_common_hobbies(data: str) -> tuple | None:
    """
    Find a pair of people who have the highest ratio of common to different hobbies.

    Common hobbies are the ones that both people have.
    Different hobbies are the ones that only one person has.

    Example:
    John has:
        running
        walking
    Mary has:
        dancing
        running
    Nora has:
        running
        singing
        dancing

    Pairs and corresponding common and different hobbies; ratio
    John and Mary; common: running; diff: walking, dancing; ratio: 1/2
    John and Nora; common: running; diff: walking, singing, dancing; ratio: 1/3
    Mary and Nora; common: running, dancing; diff: singing; ratio: 2/1

    So the best result is Mary and Nora. It doesn't matter in which order the names are returned.

    If multiple pairs have the same best ratio, it doesn't matter which pair is returned.

    The exception is when multiple pairs share all of their hobbies, in which case the pair with
    the most shared hobbies is returned.

    A pair with only common hobbies is better than any other pair with at least 1 different hobby.

    Example:
    John has:
        running
        walking
    Mary has:
        running
        walking
    Nora has:
        running
    Oprah has:
        running
    Albert has:
        tennis
        basketball
        football
    Xena has:
        tennis
        basketball
        football
        dancing

    John and Mary have 2 common, 0 different. Ratio 2/0
    Nora and Mary (also Nora and John, Oprah and John, Oprah and Mary) have 1 common, 1 different. Ratio 1/1
    Nora and Oprah have 1 common, 0 different. Ratio 1/0
    Albert and Xena have 3 common, 1 different. Ratio 3/1

    In that case the best pair is John and Mary. If the number of different hobbies is 0,
    then this is better than any pair with at least 1 different hobby.
    Out of the pairs with 0 different hobbies, the one with the highest number
    of common hobbies is the best.
    If there are multiple pairs with the highest number of common hobbies,
    any pair (and in any order) is accepted.

    If there are less than 2 people in the input, return None.
    """
    people_hobbies: dict[str, list[str]] = create_dictionary(data)

    if len(people_hobbies) < 2:
        return None

    people_pairs = list(itertools.combinations(people_hobbies.keys(), 2))
    people_pairs_ratio: dict[tuple[str, str], fractions.Fraction] = dict()
    for pair in people_pairs:
        person_a, person_b = pair
        hobbies_count = collections.Counter(people_hobbies[person_a] + people_hobbies[person_b])
        common_hobbies = [hobby for hobby, count in hobbies_count.items() if count == 2]
        distinct_hobbies = [hobby for hobby, count in hobbies_count.items() if count == 1]
        people_pairs_ratio[pair] = fractions.Fraction(len(common_hobbies), len(distinct_hobbies) + 1)

    return max(people_pairs_ratio, key=lambda key: (people_pairs_ratio[key], people_pairs_ratio[key].numerator))


if __name__ == '__main__':
    sample_data = """Jack:crafting\nPeter:hiking\nWendy:gaming\nMonica:tennis\nChris:origami\nSophie:sport\nMonica:design\nCarmen:sport\nChris:sport\nMonica:skateboarding\nCarmen:cooking\nWendy:photography\nMonica:tennis\nCooper:yoga\nWendy:sport\nCooper:movies\nMonica:theatre\nCooper:yoga\nChris:gaming\nMolly:fishing\nJack:skateboarding\nWendy:fishing\nJack:drawing\nMonica:baking\nSophie:baking\nAlfred:driving\nAlfred:shopping\nAlfred:crafting\nJack:drawing\nCarmen:shopping\nCarmen:driving\nPeter:drawing\nCarmen:shopping\nWendy:fitness\nAlfred:travel\nJack:origami\nSophie:design\nJack:pets\nCarmen:dance\nAlfred:baking\nSophie:sport\nPeter:gaming\nJack:skateboarding\nCooper:football\nAlfred:sport\nCooper:fitness\nChris:yoga\nWendy:football\nMolly:design\nJack:hiking\nMonica:pets\nCarmen:photography\nJack:baking\nPeter:driving\nChris:driving\nCarmen:driving\nPeter:theatre\nMolly:hiking\nWendy:puzzles\nJack:crafting\nPeter:photography\nCarmen:theatre\nSophie:crafting\nCarmen:cooking\nAlfred:gaming\nPeter:theatre\nCooper:hiking\nChris:football\nChris:pets\nJack:football\nMonica:skateboarding\nChris:driving\nCarmen:pets\nCooper:gaming\nChris:hiking\nJack:cooking\nPeter:fishing\nJack:gaming\nPeter:origami\nCarmen:movies\nSophie:driving\nJack:sport\nCarmen:theatre\nWendy:shopping\nCarmen:pets\nWendy:gaming\nSophie:football\nWendy:theatre\nCarmen:football\nMolly:theatre\nPeter:theatre\nMonica:flowers\nMolly:skateboarding\nPeter:driving\nSophie:travel\nMonica:photography\nCooper:cooking\nJack:fitness\nPeter:cooking\nChris:gaming"""
    sort_result = sort_names_and_hobbies(sample_data)
    # if the condition after assert is False, error will be thrown
    assert isinstance(sort_result, tuple)
    assert len(sort_result) == 10
    assert sort_result[0][0] == 'Alfred'
    assert len(sort_result[0][1]) == 7
    assert sort_result[-1] == ('Wendy', ('fishing', 'fitness', 'football', 'gaming', 'photography', 'puzzles', 'shopping', 'sport', 'theatre'))
    # if you see this line below, then everything seems to be ok!
    print("sorting works!")

    sample_data = """Jack:painting\nPeter:painting\nJack:running\nMary:running\nSmith:walking"""
    print(find_people_with_hobbies(sample_data, ["running", "painting"]))
    print(find_people_with_hobbies(
        "John:running\nMary:running\nJohn:dancing\nJack:dancing\nJack:painting\nSmith:painting",
        ["running", "dancing"]
    ))  # {"John", "Mary", "Jack"}

    sample_data = """John:running\nJohn:walking\nMary:dancing\nMary:running\nNora:running\nNora:singing\nNora:dancing"""
    print(find_two_people_with_most_common_hobbies(sample_data))  # ('Mary', 'Nora')
    print(find_two_people_with_most_common_hobbies(sample_data))  # ('Mary', 'Nora')
