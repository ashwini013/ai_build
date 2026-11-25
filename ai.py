import tiktoken

enc = tiktoken.get_encoding("o200k_base")

text = "I love AI"
ids= enc.encode(text)
print(ids)