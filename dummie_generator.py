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

    """!!! TODO: page_id !!!"""

    # ad meta data to tree
    date = read_marc.get_date(marc)
    title = date.replace(".", "-") + "_"
    authors = read_marc.get_author(marc)
    author_string = get_name_string(authors)
    title = title + author_string + "-"
    recipients = read_marc.get_recipient(marc)
    recipient_string = get_name_string(recipients)
    title = title + recipient_string
    root.set("title", title)
    root.set("catalogue_id", id)
    root.set("date", date)

    elem = root[0]
    e_author = etree.Element("author")
    for author in authors:
        print("autor: {}".format(author))
        e_p = etree.Element("person")
        e_author.append(e_p)
        e_gnd = etree.Element("gnd")
        e_p.append(e_gnd)
    elem.append(e_author)

    for r in recipients:
        print("recipient: {}".format(r))

    print(etree.tostring(root, pretty_print=True))

    # generate file name
    filename = "testfile.xml"

    write_file(tree, filename)

    print("done writing file to disk.")


def write_file(tree, filename):
    print("Writing file: {}".format(filename))

    with open("output/xml/" + filename, "wb") as out_file:
        out_file.write(etree.tostring(tree, pretty_print=True))


def get_name_string(pp):
    names = ""
    for p in pp:
        n = p.get("name")
        n = n.replace(",", "")
        n = n.replace(".", "")
        n = n.replace("'", "")
        n = n.replace(" ", "_")
        names = n + "-"
    names = names[0:-1]
    return names


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


