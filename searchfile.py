# coding: utf-8
import os
import re

directoryBaseOfSearch = os.path.dirname(os.path.realpath(__file__))+'/c-test-files'
termOfQueryPastes = ['1', '2']

def chooseMonthOfSearch():
    ano = '2019'
    mes = '05'
    return ano + '/' + mes + '.' + ano

def returnListOfPastesForSearch():
    listOfPastesOfCompanys = []
    monthOfSearch = chooseMonthOfSearch()
    for index in os.listdir(directoryBaseOfSearch):
        listOfPastesOfCompanys.append( directoryBaseOfSearch + '/' + index + '/FISCAL' + '/' + monthOfSearch + '/Declaração')
    return listOfPastesOfCompanys


def searchFileInDirectory():
    listOfPastesOfCompanys = returnListOfPastesForSearch()
    for item in listOfPastesOfCompanys:
        print( item )
        print (item  + '/' + 'doc.html' )
        print(os.path.isfile(item + '/' + 'doc.html' )) #posso usar uma REGEX aqui

searchFileInDirectory()