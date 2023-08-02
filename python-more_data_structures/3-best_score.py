#!/usr/bin/python3
def best_score(a_dictionary=None):
    if a_dictionary == None:
        return None
    else:
        sorted_dictionary = sorted(a_dictionary.items(), key=lambda x: x[1])
        return sorted_dictionary[-1][0]


def main():
    a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
    best_key = best_score(a_dictionary)
    print("Best score: {}".format(best_key))

    best_key = best_score(None)
    print("Best score: {}".format(best_key))

    pass


if __name__ == "__main__":
    main()
