hash_string = "6dsf57dsff53cbxv283trze733zer2847hgfd9328ghj38ghfj47hgk3jhkg72kg797kg6hkjg32ghjk863kgh26khg76jhgk5gk833gk27khgk76jgk583kg32hkjg74696gbnmkjh8terw787tew984tewr7585"

numbers = ""
for i in range(len(hash_string)):
    if hash_string[i].isdigit() == True:
        numbers += (hash_string[i])

for i in range(0, len(numbers), 2):
    number = int(numbers[i]+(numbers[i+1]))
    print(chr(number), end="")

