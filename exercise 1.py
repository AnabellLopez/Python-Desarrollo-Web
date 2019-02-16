import requests
import re
url = 'https://www.gutenberg.org/files/2638/2638-0.txt'
T = requests.get(url).text

start = re.search(r'I\.', T).end()
end = re.search(r'II\.', T).start()

print(T[start:end])
