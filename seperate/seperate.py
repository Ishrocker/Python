'''
accepts a list of dictionaries

for a givien key, will create a new list for every unique value in that key

for example
a = [
        {'id': '1', 'name': 'Steven'},
        {'id': '2', 'name': 'Tom'},
        {'id': '2', 'name': 'Rob'}
    ]

x = Seperate.uniqueValues(a, 'id')
print(x)
[
    [
        {'id': '1', 'name': 'Steven'}
    ],
    [
        {'id': '2', 'name': 'Tom'},
        {'id': '2', 'name': 'Rob'}
    ]
]


'''


class Seperate(object):
    def uniqueValues(a_list, key):
        '''
        accepts a list of dictionaries and a key for the dictionary

        returns a list containing containing list of dictinaries
        seperated by unique values in key
        '''

        def _seperateByKey(a_list, key, value) -> list:
            '''
            accepts a list of dictionaries, a dictionary key, and value

            returns a new list of dictionaries
            where the value of the key equaled the passed value
            '''
            a = [x for x in a_list if x[key] == value]
            return a

        def _getUniqueValues(a_list, key) -> set:
            '''
            returns set of unique values in key

            '''
            s = set([x[key] for x in a_list])
            return s

        z = _getUniqueValues(a_list, key)
        tmp = [_seperateByKey(a_list, key, x) for x in z]
        return tmp
