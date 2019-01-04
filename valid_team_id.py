from bs4 import BeautifulSoup
import urllib.request
import re
import sys
sys.setrecursionlimit(1000000000)
with open("current_id.txt",'r') as out:
    id_number = int((out.read()))
def loop(id_number):
    while True:
        #if (len(str(id_number)) == 9):
            #break;
        url = "https://play.eslgaming.com/team/matches/" + str(id_number)
        id = re.sub('\D',"", url)
        with open("current_id.txt", 'w') as out:
            out.write(str(id))
        link = urllib.request.urlopen(url).read()
        game = 0
        soup = BeautifulSoup(link, 'html.parser')
        if "matches" in url:
            error = (soup.find_all("strong"))
            text = (soup.find_all("td"))
        else:
            text = (soup.find_all("b"))
            error = (soup.find_all("strong"))
        error = str(error)
        clean_error = error
        clean_error = "".join(clean_error.split())
        clean_error_len = len(clean_error)
        for counter in range(clean_error_len):
            if error[counter:counter + 6] == "Error:":
                id_number = id_number + 1
                loop(id_number)
        text = str(text)
        print (id)
        clean = text
        clean = "".join(clean.split())
        clean_len = len(clean)
        for counter in range(clean_len):
            if clean[counter:counter + 17] == "bgcolor=" + '"#7BA37F"':
                game = game + 1
            elif clean[counter:counter + 17] == "bgcolor=" + '"#EEE295"':
                game = game + 1
            elif clean[counter:counter + 17] == "bgcolor=" + '"#AC6060"':
                game = game + 1
        if (game >= 1):
            with open("valid_teams.txt", 'a') as out:
                out.write("\n" + str(id))
        id_number = id_number + 1
loop(id_number)
