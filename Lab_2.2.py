def process_input(data):

    if type(data) == list:
        return sum(data) / len(data)
    elif type(data) == dict:
        return dict(sorted(data.items(), key=lambda x: x[1]))
    elif type(data) == int:
        return int(str(data)[::-1])
    elif type(data) == str:
        words = data.split()
        longest_word = max(words, key=len)
        return {"word_count": len(words), "longest_word": longest_word}
    else:
        return None


result = process_input([1, 2, 3, 4, 5])
print(result) # 3.0

result = process_input({"a": 10, "b": 5, "c": 20})
print(result) # {"b": 5, "a": 10, "c": 20}

print(process_input(12345))# 54321

result = process_input("Hello world")
print(result) # {"word_count": 2, "longest_word": "Hello"}