import collections

Scientist = collections.namedtuple(
    'Scientist', ['name', 'field', 'born', 'nobel'])

scientists = (
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
    Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
    Scientist(name='Tu Youyou', field='chemistry', born=1930, nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
    Scientist(name='Vera Rubin', field='astronomy', born=1928, nobel=False),
    Scientist(name='Sally Ride', field='physics', born=1951, nobel=False)
)

def nobel_filter(x):
    return x.nobel is True

# filter and lamda
result = tuple(filter(lambda x: x.nobel, scientists))
# filter and function
result_f = tuple(filter(nobel_filter, scientists))
# list comprehesion
result_c = [x for x in scientists if x.nobel is True]
result_ct = tuple(x for x in scientists if x.nobel is True)
result2 = tuple(filter(lambda x: x.field == 'physics' and x.nobel, scientists))

print(result)
print(result_f)
print(result_c)
print(result_ct)
print(result2)
