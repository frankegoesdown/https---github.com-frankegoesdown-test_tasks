# __author__ = 'a.chernikov'


# test values

#standart lists
#keys = [1,2,3]
#values = [4,5,6]

#without key
#keys = [1,2]
#values = [4,5,6]

#without value
keys = [1, 2, 3]
values = [4, 5]

#empty lists
#keys = []
#values = []

def zip_map(keys, values):
    res = {}
    it = iter(values)
    nullValue = False
    for key in keys:
        try:
            res[key] = it.next() if not nullValue else None
        except StopIteration:
            nullValue = True
            res[key] = None
    return res


def zip_map2(k, v):
    v.extend([None for i in range(len(v), len(k))])
    return dict(zip(k, v))


print zip_map(keys, values)
print zip_map2(keys, values)

print dict((len(keys) > len(values)) and map(None, keys, values) or zip(keys, values))



