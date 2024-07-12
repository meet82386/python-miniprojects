from bs4 import BeautifulSoup

def getdata(filepath):
    with open(filepath) as file:
        HTMLString= file.read()
    bs = BeautifulSoup(HTMLString, "html.parser")
    tags = bs.find_all("a")
    data_list = []
    for tag in tags:
        data_list.append(tag.getText())
    return data_list

followers = getdata("connections/followers_and_following/followers_1.html")
following = getdata("connections/followers_and_following/following.html")

print("Peoples who do not follow back you: ")
for i in following:
    if i not in followers:
        print(i)