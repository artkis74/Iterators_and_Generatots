from Iterator import FlatIterator
nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
]

# print(list(chain.from_iterable(nested_list)))
if __name__ == '__main__':
        for item in FlatIterator(nested_list):
                print(item)
        flat_list = [item for item in FlatIterator(nested_list)]
        print(flat_list)