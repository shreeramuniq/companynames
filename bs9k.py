import urllib2
from bs4 import BeautifulSoup as BS
import re

fil_dir = open('D:\\bs9k\\9000_dir_details_sep22.txt', "a+")
fil_com = open('D:\\bs9k\\9000_company_addr_sep22.txt', "a+")

director_ucc = {}
with open('D:\\bs9k\\9000_ucc_zauba_sep22.txt') as fil:
     for line in fil:
         key,val = line.strip('\n').split('|')
         director_ucc[int(key)]=val
for k,v in director_ucc.iteritems():
   r = urllib2.urlopen(v).read()
   soup = BS(r,'lxml')
   print k
   for row in soup.findAll('table', attrs={'class' : 'table table-striped'})[0].thead.findAll('tr'):
    addr = []   
    addr.append(row.text[3:])
    for i,item in enumerate(soup.findAll('div', attrs={'class' : 'col-lg-6 col-md-6 col-sm-12 col-xs-12'})[2]):
     if i == 0 :
      addr.append(item.text[item.text.find(':')+1:]),addr.append(item.text[item.text.find('@')+1:])
     if i == 3:
      addr.append(item.text)
      print addr
      data_format = "|".join( str(repr(e)) for e in addr )
      print data_format
      st = str(str(k) +"|" + data_format  + "\n")
      fil_com.write(st)
    for row in soup.findAll('table', attrs={'class' : 'table table-striped'})[7].tbody.findAll('tr'):
     details = []
     for data in row.findAll('td'):
       details.append(data.text)
       if len(details) == 4 and details[0].find('Compan') == -1:
         details = [details[1],details[2]]
         data_format1 = "|".join( repr(e) for e in details )
         print data_format1
         st1 = str(str(k) +"|" + data_format1 + "\n")
         fil_dir.write(st1)
'''
   for row in soup.findAll('table', attrs={'class' : 'table table-striped'})[0].thead.findAll('tr'):
    addr = []   
    addr.append(row.text[3:])
    for i,item in enumerate(soup.findAll('div', attrs={'class' : 'col-lg-6 col-md-6 col-sm-12 col-xs-12'})[2]):
     if i == 0 :
      addr.append(item.text[item.text.find(':')+1:]),addr.append(item.text[item.text.find('@')+1:])
     if i == 3:
      addr.append(item.text)
      print addr
      data_format = "|".join( repr(e) for e in addr )
      print data_format
      st = str(data_format)
      fil.write(st + "\n")
'''
fil_dir.close()
fil_com.close()





   
