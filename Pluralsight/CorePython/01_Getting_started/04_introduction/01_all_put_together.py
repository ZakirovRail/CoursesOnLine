from urllib.request import urlopen

story = urlopen('http://sixty-north.com/c/t.txt')
story_words = []
for line in story:
    line_words = line.decode('utf-8').split()  # to decode
    for word in line_words:
        story_words.append(word)
story.close()
print(story_words)


# ===============================================
from urllib.request import urlopen

story = urlopen('http://sixty-north.com/c/t.txt')  # to get a result as a bytes data
story_words = []
for line in story:
    line_words = line.split()
    for word in line_words:
        story_words.append(word)
story.close()
print(story_words)