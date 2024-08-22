'''
Description:

Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet" 

'''
# My solution
def domain_name(url):
    listUrl = url.split('//')
    for i in listUrl:
        newList = i.split('.')
    if 'www' in newList:
        newList.remove('www')
    return newList[0]

'''
Good solution

def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

'''
