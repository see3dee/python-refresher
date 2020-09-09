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









print("done")


