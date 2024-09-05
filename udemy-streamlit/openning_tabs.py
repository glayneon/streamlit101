import webbrowser
with open('./links.txt') as file:
    links = file.readlines()
    for _, link in enumerate(links):
        webbrowser.open(link)