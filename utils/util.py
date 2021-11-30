import requests

def ReadFileIntoList(filename):
    with open("test.txt") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def ReadRequestIntoList(url):
    response = requests.get(url)
    return response.content