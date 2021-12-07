# put your python code here
words = input().lower().split()
freq_dict = {word: words.count(word) for word in words}
for item in freq_dict.items():
    print(item[0], item[1])
