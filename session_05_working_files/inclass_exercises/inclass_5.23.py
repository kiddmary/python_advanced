# 5.23:  Given the following dict of dicts, sort the dict keys by the last name.
# Loop through and print each key.

people = {  '12345': { 'fname':  'Joe',
                       'lname':  'Wilson',
                       'addr':   '12345 Main Street' },

            '00355': { 'fname':  'Marie',
                       'lname':  'Adams',
                       'addr':   '888 Elm Street' },

            '98973': { 'fname':  'Alex',
                       'lname':  'Wilson',
                       'addr':   '23 Marsh Avenue' }
}
def dict_by_dict_addr(dict_key):
    return people[dict_key]['lname']

skeys = sorted(people, key=dict_by_dict_addr)

print(skeys)