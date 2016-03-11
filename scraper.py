from bs4 import BeautifulSoup
import sys


if len(sys.argv) > 3:
    divisor = int(sys.argv[3])
else:
    divisor = 1
hacker_to_msu = {}

with open("coursesurvey.csv") as infile:
    
    infile.readline()
    for line in infile:
        sline = line.split(",")
        if len(sline) > 4:
            hacker_to_msu[sline[4].strip('"')] = sline[3].strip('"')
        
print(hacker_to_msu)

with open(sys.argv[1]) as infile:
    html = infile.read()


grades_file = open(sys.argv[2], "w")
grades_file.write("Username, HW #3 Points Grade, End-of-Line Indicator\n")

soup = BeautifulSoup(html, "html.parser")
#leaders = soup.find(id="leaders")
leaders = soup.find_all("div", "leaderboard-list-view")
for el in leaders:
    pars = el.find_all("p")
    student = str(pars[1].a.string).strip()
    
    #Josh was just testing
    if student == "joshua_nahum":
        continue
    student = hacker_to_msu[student]
    grade = str(float(str(pars[3].string).strip())/divisor)
    grades_file.write(",".join([student, grade, "#"])+"\n")
    print(student, grade)
    
grades_file.close()
