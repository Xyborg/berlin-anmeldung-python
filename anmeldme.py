#----------------------------------------------------------------------------
# Created By  : Martin Aberastegue (Twitter: @Xyborg)
# Created Date: 15.10.2021
# version ='1.7'
# FYI: I am not an expert Python developer, I did this just for fun. Feel free
# to fork it or make any suggestions/adjustments.
# You can add an integration to a Slack channel or send an email, whatever you
# like from this code. Just be creative, so you don't have to stare at your
# screen waiting for that damn free appointment.
# ---------------------------------------------------------------------------
import re
import random
import time
import datetime
from user_agent import generate_user_agent, generate_navigator
import requests
from bs4 import BeautifulSoup

sleept_st = 40
sleept_to = 65
print("Getting ready to parse content...\n")
while True:
    # Initial URL request to get the cookie before we proceed, otherwise, the server will block us from the beginning.
    tag_url = "https://service.berlin.de/terminvereinbarung/termin/tag.php?termin=1&anliegen[]=120686&dienstleisterlist=122210,122217,327316,122219,327312,122227,327314,122231,122243,122252,329742,122260,329745,122262,329748,122254,329751,122271,327278,122273,327274,122277,327276,330436,122280,327294,122282,327290,122284,327292,327539,122291,327270,122285,327266,122286,327264,122296,327268,150230,329760,122301,327282,122297,327286,122294,327284,122312,329763,122314,329775,122304,327330,122311,327334,122309,327332,122281,327352,122279,329772,122276,327324,122274,327326,122267,329766,122246,327318,122251,327320,122257,327322,122208,327298,122226,327300&herkunft=https%3A%2F%2Fservice.berlin.de%2F"
    ua = generate_user_agent()
    headers = {'Content-Type': 'text/html; charset=utf-8',
                'User-Agent':str(ua),
                'pragma': 'no-cache',
                'content-encoding': 'gzip, deflate, br',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'referer': 'https://service.berlin.de/terminvereinbarung/',
                }      
    res = requests.get(tag_url, headers=headers, allow_redirects=False)
    if res.status_code == 302:
        cookiejar = res.cookies
        t_url = "https://service.berlin.de"+res.headers['Location']

        print("Trying page 1: ", t_url)
        html_text = requests.get(t_url, headers=headers, cookies=cookiejar).text
        soup = BeautifulSoup(html_text, 'html.parser')
        termin_links_p1 = soup.find_all('a', href = re.compile("terminvereinbarung/termin/time"))
        termin_tiemstamp = datetime.datetime.fromtimestamp(time.time()) + datetime.timedelta(days=17)
        t_url_p2 = "https://service.berlin.de/terminvereinbarung/termin/day/" + str(int(termin_tiemstamp.timestamp())) + "/"
        print("Trying page 2: ", t_url_p2)
        html_text = requests.get(t_url_p2, headers=headers, cookies=cookiejar).text
        soup = BeautifulSoup(html_text, 'html.parser')
        termin_links_p2 = soup.find_all('a', href = re.compile("terminvereinbarung/termin/time"))
        termin_links = termin_links_p1 + termin_links_p2
        tfound = len(termin_links)
        if tfound > 0:
            print("\n#######################################################\n")
            print("I found ", tfound ," avialable appointments!:\n")
            print("#######################################################\n")
            mylist = list(dict.fromkeys(termin_links))
            for link in termin_links:
                # Quick and dirty way to get the date from the appointment path
                st = re.findall(r'\d+', link.get('href'))
                date_termin = time.strftime("%d-%m-%Y", time.localtime(int(st[0])))
                # that way we are able to print it in a human readable format along with the full link:
                print(date_termin+": https://service.berlin.de"+link.get('href'))
            print("\nHurry! Copy the links and book your termin now.\n")
            break
        else:
            print(datetime.datetime.now().strftime("%H:%M:%S"), "> I couldn't find any available termin :(\n")
    else:
        print("If you see this, probably you got blocked by the server. Try later in a few minutes...")
        break
    # If we keep this as a loop, we add some sleep time between request so we don't get blocked.
    # You can comment the following line, but I would suggest leaving it like this or even try increasing
    # the number of seconds if you get constantly banned by the site for making too many requests.
    time.sleep(random.uniform(sleept_st, sleept_to))
