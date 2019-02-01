#import aleph_request


def generate_all():
    print("\n\n\ngenerating...\n")
    all_numbers = get_all_numbers()
    existing_numbers = get_existing_numbers()
    #aleph_request.


def get_all_numbers():
    print("\nfetching list of all system numbers...")
    res = get_list("input/all_numbers.txt")
    print("done fetching all numbers.\n")
    return res


def get_existing_numbers():
    print("fetching list of system numbers that already have a letter...")
    res = get_list("input/existing_numbers.txt")
    print("done fetching existing numbers.")
    return res


def get_list(path):
    print("fetching list in path: {}".format(path))
    res = []
    with open(path) as f:
        res = f.readlines()
    print(res)
    return res




