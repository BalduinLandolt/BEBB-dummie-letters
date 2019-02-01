from pymarc import MARCReader

def read_mc_test():
    print("reading example")
    read_mc("000054744")


def read_mc(sys_no):
    print("reading: "+sys_no)
    list = []
    with open("input/aleph_data/"+sys_no+".marc", "rb") as f:
        print(f)
        data = f.read()
    print(data)
    reader = MARCReader(bytes(data), force_utf8=True, to_unicode=True)
    print(reader)
    tmp = next(reader)
    print(tmp)
    print("date:")
    print(get_date(tmp))

def get_date(records):
    date = None
    for field in records.get_fields('046'):
        date = field['c']

    return date

