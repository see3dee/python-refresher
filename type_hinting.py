from typing import List

# def list_ave(sequence):
#     return sum(sequence) / len(sequence)
#
#
# seq = (1, 2, 3, 4, 5, 6, 7)
# seq2 = [1, 2, 3, 4, 5, 6, 7]
#
# print(f" The average of this sequence is {list_ave(seq2)}")


def list_ave(sequence: List) -> float:
    return sum(sequence) / len(sequence)


seq = (1, 2, 3, 4, 5, 6, 7)
seq2 = [1, 2, 3, 4, 6, 6, 7]

print(f" The average of this sequence is {list_ave(seq)}")

list_ave(seq)