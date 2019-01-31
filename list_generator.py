import os
import lxml
from os import listdir
from lxml import etree


def get_by_name(name):
    print("trying to load data by name ("+name+")...")
    prefix = "input/xml/"
    sysNo = ""
    try:
        root = etree.parse(prefix + name, etree.XMLParser(load_dtd=True)).getroot()
        print(etree.tostring(root))
        sysNo = root.get("catalogue_id")
        print(sysNo)
        print("got file by name.\n")
    except OSError:
        print("Could not read File: " + name + "\n")
    return sysNo


def create_list_of_existing_system_numbers():
    if os.path.isfile("./input/existing_numbers.txt"):
        print("output file already exists.\nabort.")
        return

    print("getting a list of the contents of the directory...")
    files = listdir("input/xml")
    print("found:")
    print(files)
    print()
    res = ""
    for file in files:
        print(file)
        sys_no = get_by_name(file.__str__())
        res += sys_no + "\n"

    print("Result: ")
    print(res)
    with open("input/existing_numbers.txt", "w") as out_file:
        print(res, file=out_file)

    print("handled all files in folder.")



def load_all_numbers():
    print("loading numbers...")
    res = []
    with open("input/all_numbers.txt") as f:
        res = f.readlines()
    print("found numbers: " + str(res.__sizeof__()))
