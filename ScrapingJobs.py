import urllib.request as url
import bs4

path = "https://www.freshersworld.com/jobs/jobsearch/python-jobs"

response = url.urlopen(path)
page = bs4.BeautifulSoup(response)

# span = page.find('span', {'class' : 'wrap-title'})
# print(span.text)

span = page.find_all('span', {'class' : 'wrap-title'})
location = page.find_all('span', {'class' : 'job-location'})
qualifications = page.find_all('span', {'class' : 'qualifications'})
for i in range(len(span)):
    print("Job Title :", span[i].text)
    print("Location :",location[i].text)
    print("Qualification :",qualifications[i].text)
    print("*" * 50)