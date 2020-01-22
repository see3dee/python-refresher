string_input = "aaabbbbccdff"
comp_str = " "
char_cnt = 0
i = 0
for char in string_input:
        if char == string_input[i+1]:
            print(f" {char} {string_input[i + 1]} {i} {char_cnt}")
            char_cnt += 1
            i += 1
        else:
            print(f" {char} {string_input[i + 1]} {i} {char_cnt}")
            print(f" {string_input[i]} {char_cnt}")
            char_cnt = 0






