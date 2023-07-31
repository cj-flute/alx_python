#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_sentence = tuple(list(sentence))
    if sentence == "":
        empty_string = "None"
        return len(sentence), empty_string
    return len(tuple_sentence), tuple_sentence[0]
    pass


def main():
    sentence = input()
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))
    pass


if __name__ == "__main__":
    main()
