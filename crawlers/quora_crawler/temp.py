import requests
from database import get_all_content

result = get_all_content()

word = 0

for content in result:
    count = len(content["text"].split(" "))
    word += count
    
    
print(f"The total number of words is: {word / len(result)}")