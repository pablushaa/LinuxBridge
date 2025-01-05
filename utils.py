import requests

def downloadCat() -> None:
    req = requests.get("https://cataas.com/cat")
    with open("cat.jpg", "wb") as file: file.write(req.content)