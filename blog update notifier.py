import requests
from bs4 import BeautifulSoup

urls = ["https://sites.google.com/view/noahhi-reu/home","https://sites.google.com/asu.edu/reu2019/home",
"https://sites.google.com/yale.edu/eslaughter-reu","https://sites.google.com/view/anlans-reu-blog/home",
"https://sites.google.com/iu.edu/ciabhans-blog/home","https://sites.google.com/view/niccivyea-reu/home",
"https://sites.google.com/view/devexpdesignlab/home","https://sites.google.com/view/peter-cherniavsky-reu-2019/home",
"https://sites.google.com/view/abhi-reu/home?authuser=0"]

current_lengths = []
for url in urls:
    r = requests.get(url)
    soup = BeautifulSoup(r.content,features="html.parser")
    body = soup.find('body')
    current_lengths.append(str(len(body.text)))

with open('blog_lengths.txt','r') as file:
    contents = file.read()
    prev_lengths = contents.split(',')
    for i in range(len(prev_lengths)):
        prev_length = prev_lengths[i]
        current_length = current_lengths[i]
        diff = abs(int(prev_length) - int(current_length))
        url = urls[i]
        if diff > 0:
            print('changed : ' + str(diff) + ' : ' + url)
        else:
            print('same : ', url)


with open('blog_lengths.txt','w') as file:
    file.write(','.join(current_lengths))
