from pymarc import MARCReader

def read_mc_test():
    print("reading example")
    read_mc("000054744")
    read_mc("000054745")


def read_mc(sys_no):
    print("reading: "+sys_no)
    list = []
    with open("input/aleph_data/"+sys_no+".marc", "rb") as f:
        print(f)
        data = f.read()
    #print(data)
    reader = MARCReader(bytes(data), force_utf8=True, to_unicode=True)
    #print(reader)
    tmp = next(reader)
    print(tmp)
    #print("date:")
    #print(get_date(tmp))
    return tmp

def get_date(records):
    date = None
    for field in records.get_fields('046'):
        date = field['c']

    return date

def __check_for_gnd(marcField, GNDIndex):

    if marcField['d'] is not None:
        date = marcField['d']
    else:
        date = ""

    if marcField[GNDIndex] is None:
        GND = 'no_GND'
    else:
        # get rid of trailing comma
        GND = marcField[GNDIndex].replace(',', '')

    role = ""
    if marcField['4'] is not None:
        role = marcField['4']

    return {
        "GND": GND,
        "name": marcField['a'],
        "date": date,
        "role": role
    }

def get_author(records):
    author = []
    for field in records.get_fields('100'):
        author.append(__check_for_gnd(field, '0'))

    # check for 700 that are actually authors
    for field in records.get_fields('700'):
        person = __check_for_gnd(field, '0')

        if person['role'] == "aut":
            author.append(person)

    return author

def get_recipient(records):
    recipient = []
    for field in records.get_fields('700'):
        person = __check_for_gnd(field, '0')

        if person['role'] == "rcp":
            recipient.append(person)

    return recipient

def get_mentioned_persons(records):
    mentioned = []
    for field in records.get_fields('600'):
        mentioned.append(__check_for_gnd(field, '0'))

    return mentioned

def get_description(records):
    description = None
    for field in records.get_fields('245'):
        if 'a' in field:
            description = {
                'title': field['a']
            }

        if 'c' in field:
            if description is not None:
                description.update({
                    'author': field['c']
                })
            else:
                description = {
                    'author': field['c']
                }

    return description

def get_creation_form(records):
    creation_information = None
    for field in records.get_fields('250'):
        if 'a' in field:
            creation_information = field['a']

    return creation_information

def get_creation_place(records):
    creation_place = None
    for field in records.get_fields('751'):
        if 'a' in field:
            creation_place = {
                'place': field['a']
            }
        if '0' in field:
            if creation_place is not None:
                creation_place.update({
                    'gnd': field['0']
                })
            else:
                creation_place = {
                    'gnd': field['0']
                }


    return creation_place

def get_physical_description(records):
    physical_description = None
    for field in records.get_fields('300'):
        if 'a' in field:
            physical_description = {
                'amount': field['a']
            }

        if 'c' in field:
            if physical_description is not None:
                physical_description.update({
                    'format': field['c']
                })
            else:
                physical_description = {
                    'format': field['c']
                }

    return physical_description

def get_footnote(records):
    footnote = None
    for field in records.get_fields('500'):
        if 'a' in field:
            footnote = field['a']

    return footnote

def get_bibliographical_info(records):
    bibliographical_info = None
    for field in records.get_fields('510'):
        if 'a' in field:
            bibliographical_info = {
                'reference': field['a']
            }

        if 'i' in field:
            if bibliographical_info is not None:
                bibliographical_info.update({
                    'type': field['i']
                })
            else:
                bibliographical_info = {
                    'type': field['i']
                }

    return bibliographical_info

def get_content_info(records):
    content_info = None
    for field in records.get_fields('520'):
        if 'a' in field:
            content_info = field['a']

    return content_info

def get_accompanying_material(records):
    accompanying_material = None
    for field in records.get_fields('525'):
        if 'a' in field:
            accompanying_material = field['a']

    return accompanying_material

def get_reproduction_info(records):
    reproduction_info = None
    for field in records.get_fields('533'):
        if 'a' in field:
            reproduction_info = {
                'type': field['a']
            }

        if 'b' in field:
            if reproduction_info is not None:
                reproduction_info.update({
                    'place': field['b']
                })
            else:
                reproduction_info = {
                    'place': field['b']
                }

        if 'c' in field:
            if reproduction_info is not None:
                reproduction_info.update({
                    'institution': field['c']
                })
            else:
                reproduction_info = {
                    'institution': field['c']
                }

        if 'd' in field:
            if reproduction_info is not None:
                reproduction_info.update({
                    'year': field['d']
                })
            else:
                reproduction_info = {
                    'year': field['d']
                }

        if 'n' in field:
            if reproduction_info is not None:
                reproduction_info.update({
                    'additional': field['n']
                })
            else:
                reproduction_info = {
                    'additional': field['n']
                }

    return reproduction_info

def get_language(records):
    language = None
    for field in records.get_fields('546'):
        if 'a' in field:
            language = field['a']

    return language

def get_bernoulli_work_reference(records):
    bernoulli_work_reference = None
    for field in records.get_fields('596'):
        if 'a' in field:
            bernoulli_work_reference = field['a']

    return bernoulli_work_reference

def get_emanuscript_link(records):
    emanuscript_link = None
    for field in records.get_fields('856'):
        if 'u' in field:
            emanuscript_link = field['u']

    return emanuscript_link
