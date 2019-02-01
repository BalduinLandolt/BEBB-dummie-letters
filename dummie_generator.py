import read_marc, list_generator
from lxml import etree


def generate_all():
    print("\n\n\ngenerating...\n")
    #all_numbers = get_all_numbers()
    #existing_numbers = get_existing_numbers()
    #aleph_request.
    list = list_generator.get_list("output/out_list.txt")
    timeout = 0
    for no in list:
        timeout = timeout + 1
        if timeout > 1:
            print("timeout!")
            break
        print("looking for number: "+no)
        ma = read_marc.read_mc(no)
        generate_dummie(ma, no)
        #print(ma)
        #print(read_marc.get_content_info(ma))


def generate_dummie(marc, id):
    date = read_marc.get_date(marc)
    print("\ngenerating dummie for: {} ({})".format(id, date))
    tree = etree.parse("input/xml_template.xml")
    root = tree.getroot()

    """!!! page_id !!!"""

    root.set("bla", "bli")

    print(etree.tostring(root, pretty_print=True))


"""
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

"""


