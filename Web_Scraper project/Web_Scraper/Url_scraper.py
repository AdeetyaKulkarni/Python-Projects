#PLease install besutifulsoup4 / requests / htmlparser(preistall hopefully) - Use Python 3 or above

from requests import get
from bs4 import BeautifulSoup


#main_url = "https://itunes.apple.com/us/app/bumble-meet-new-people/id930441707?mt=8"
main_url = "https://itunes.apple.com/us/app/pof-dating/id389638243?mt=8"

response = get(main_url)


html_soup = BeautifulSoup(response.text,'html.parser') #Use html5lib or html.parser
type(html_soup)
container = html_soup.find_all('div', class_ = 'we-customer-review lockup ember-view')
file = open("BumbleReviews.txt","a")
numreviews = len(container)


file.write(main_url+": : \n\n")

for i in range(0,numreviews):
    if(i%2==0):
        string  = str((container[i]).p)
        string = string[3:len(string)-4]

        #FILE Writing ::
        file.write(str(string))
        file.write("\n"+"------------------------------------------------------------------"+"\n")
        print(string)
        print("------------------------------------------------------------------"+"\n\n")


file.close()



