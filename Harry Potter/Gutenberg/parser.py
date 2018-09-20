from urllib.request import urlopen

filenames = []

with open("filenames.txt", "r") as file:
    for line in file.readlines():
        filenames.append(line)

print("Size: " + str(len(filenames)))
        
for x in range(len(filenames)):
    with urlopen(filenames[x]) as query:
        content = query.read()
        encoding = query.headers.get_content_charset("utf-8")
        text = content.decode(encoding)
    with open("GB" + str(x) + ".txt", "w", encoding="utf-8") as file:
        file.write(text)
    print("Book " + str(x) + " Complete")
    
