<<<<<<< HEAD
string_input = "aabbbc"
output_string = ""
compares = (len(string_input)-1)
print(compares)
char_cnt = 1
for i in range(0, compares):
    if string_input[i] == string_input[i+1]:
        char_cnt += 1
        print(f" first char:{string_input[i]} 2nd char:{string_input[i+1]} i = {i} count = {char_cnt}")
        output_string = output_string + string_input[i+1] + str(char_cnt)
    else:
        char_cnt = 1
        print(f" in else first char:{string_input[i]} 2nd char:{string_input[i+1]} i = {i} count = {char_cnt}")
        print(output_string)
=======
string_input = "aaabbbbccdff"
comp_str = " "
char_cnt = 0
i = 0
for char in string_input:
    if char == string_input[i]:
        print(f" {char} {string_input[i+1]} {i} {char_cnt}")
        char_cnt += 1
        i += 1
    else:
        char = string_input[i]
        print(f"{string_input[i]}, {char_cnt}")
        char_cnt = 1
>>>>>>> 9cb5d9ae21c2dea557db4f8c75814a0aaec267bb







<<<<<<< HEAD


print("done")


=======
>>>>>>> 9cb5d9ae21c2dea557db4f8c75814a0aaec267bb
