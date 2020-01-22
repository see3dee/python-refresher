string_input = "aaabbbbccdff"
len_string = (len(string_input)-1)
print(len_string)
for i in range(0, len_string):
    char_cnt = 0
    for char in string_input:
        if char == string_input[i]:
            # print(f" {char} {string_input[i]} {i} {char_cnt}")
            char_cnt += 1
        else:
            print(f" In the else {string_input[i]} {char_cnt}")




print("done")


