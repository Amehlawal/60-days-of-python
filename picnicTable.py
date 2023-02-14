#! /usr/bin/python3
#in this program we define a printPicnic() method that will take in a dictionary
#and use center(),ljust() and rjust() to display the information in a neatly aligned
# table-like format. PS: another program from automate the boring stuff with python

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth +rightWidth, '-'))
    for k,v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwich':4,'apples':12,'cups':4,'cookies':8000}
printPicnic(picnicItems,12,4)
