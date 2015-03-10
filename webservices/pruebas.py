__author__ = 'LFL'

import requests
from bs4 import BeautifulSoup

#r = requests.get('http://evangeli.net/evangelio/')
r1 = requests.get('http://www.santopedia.com/')
r2 = requests.get('http://evangeli.net/evangelio/')
soup1 = BeautifulSoup(r1.text)
soup2 = BeautifulSoup(r2.text)
soup1.findAll("ul", {"class": "saints"})
#print soup2
divTag = soup2.find("div", {"id": "evangeli_avui"})
#print divTag
#divChildren = divTag.findChildren()
divChildrenP = divTag.findAll("p")

dia_liturgico = divTag.find("p", {"class": "dia_liturgic"})
evangelio_del_dia = dia_liturgico.nextSibling.nextSibling
comentario_evangelio = divTag.find("p", {"class": "comentari_evangeli_primer"})

print "DIA LITURGICO -------------------------------------------------------------------------------------------------------"
print dia_liturgico.text
print "EVANGELIO DEL DIA -------------------------------------------------------------------------------------------------------"
print evangelio_del_dia.text
print "COMENTARIO DEL EVANGELIO -------------------------------------------------------------------------------------------------------"
print comentario_evangelio.text








