import os
import re

directoryBaseOfSearch = os.path.dirname(os.path.realpath(__file__))+'/c-test-files'
termOfQueryPastes = ['1', '2']

def returnListOfPastesForSearch():
    listOfPastesOfCompanys = []
    for index in os.listdir(directoryBaseOfSearch):
        listOfPastesOfCompanys.append( directoryBaseOfSearch + '/' + index + '/Fiscal')
    return listOfPastesOfCompanys


def searchFileInDirectory():
    listOfPastesOfCompanys = returnListOfPastesForSearch()
    for item in listOfPastesOfCompanys:
        print( item )
        print (item  + '/' + 'doc.html' )
        print(os.path.isfile(item + '/' + 'doc.html' )) #posso usar uma REGEX aqui

searchFileInDirectory()



