strtext = ["python", "alabuga", "python", "alabuga", "hr", "hr"]
str_text = {}
res = None
max_text = 0

for stri in strtext:
    if stri in str_text:
        str_text[stri] += 1
    else:
        str_text[stri] = 1

    if str_text[stri] > max_text:
        res = stri
        max_text = str_text[stri]

print("Наиболее частая строка: ", res)