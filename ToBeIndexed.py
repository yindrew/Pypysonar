# Test file that is used to test the indexer

def f(x):
    return x + 1


x = f(3)

print(x)



{
    'f': [(3, 4, 3, 5), (7, 4, 7, 5)],
    'NSf': {
        'f': (3, 4, 3, 5),
        'x': [(3, 6, 3, 7), (4, 11, 4, 12)]
    },
    'x': [(7, 0, 7, 1), (9, 6, 9, 7)]
}