string = "park"
arrayPy = [1, 2]
tuplePy = (10, 20)
setPy = {3, 4}
dictPy = {"key1" : "value1", "key2":"value2"}

for item in arrayPy:
    print(item)

for pageNumber in range(1, 130, 15):
    print("https://www.donga.search?p=" + str(pageNumber))
    #print("https://www.donga.search?p=", pageNumber, sep="") 동일함