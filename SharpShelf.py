import json
import requests
import openpyxl

#9781534318373


print("enter the isbn of the book you want the dimensions of")

isbn = input()

print("you typed \n" + isbn)

searchReq = requests.get("https://www.googleapis.com/books/v1/volumes?q=isbn:" + isbn)
searchData = searchReq.json()
bookID = searchData['items'][0]['selfLink']

bookReq = requests.get(bookID)
bookData = bookReq.json()
bookThick = bookData['volumeInfo']['dimensions']['thickness']
bookThick = float(bookThick[0:int(len(bookThick) - 2)])
print(bookThick)

with open(isbn+'data.json', 'w') as f:
    json.dump(bookData, f)