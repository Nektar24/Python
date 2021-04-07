#Nektar
#Gia na anoiksei to link :
import webbrowser
#Gia na dei ti mera kai ora einai shmera:
import datetime

# Mera kai ora poy etrekse to programma.
# Mera . (px "Monday")
# Ora. (px 12)
today = datetime.datetime.now().strftime("%A")
ora = datetime.datetime.now().hour

class Mathima:
  def __init__(self, name, link, day, starting_hour, ending_hour):
    self.name = name
    self.link = link
    self.day = day
    self.starting_hour = starting_hour
    self.ending_hour = ending_hour

list = []

#list.append( Mathima("","","",0,0) )

# MATHIMATA 4ou EKSAMINOU
list.append( Mathima("Arithmitikh Analysh kai perivalonta hlopoihshs","https://upatras-gr.zoom.us/j/99385546396?pwd=WVY0c1FQVVBjc2VIQWdiWWFsN1pWQT09","Monday",14,17) )
list.append( Mathima("Theoria Shmaton kai Systhmaton","https://upatras-gr.zoom.us/j/3189977126?pwd=a05FV3hrYnZhTDVGY3ptVE5nNElIdz09","Monday",17,19) )
list.append( Mathima("Psifiaka Hlektronika","https://teams.microsoft.com/l/team/19%3a5050395caf7f46f787e9a1943fcd842b%40thread.tacv2/conversations?groupId=a4a5fb9f-8233-4249-8d30-ad570390d224&tenantId=5a52ab58-42d0-4bb4-b3fc-713dd6822d20","Tuesday",13,15) )
list.append( Mathima("Domes Dedomenon","https://upatras-gr.zoom.us/j/92396242820?pwd=Tlk1QmNjYks3ZmFJc2UwVEtHTE0yUT09","Tuesday",15,17) )
list.append( Mathima("Arithmitikh Analysh kai perivalonta hlopoihshs","https://upatras-gr.zoom.us/j/99385546396?pwd=WVY0c1FQVVBjc2VIQWdiWWFsN1pWQT09","Tuesday",17,19) )
list.append( Mathima("Sygxrona Themata Arxitektonikhs","https://upatras-gr.zoom.us/j/98228365346?pwd=S1Y2K1FGM08zYk9JbDRPNzJwTHZPUT09#success","Wednesday",17,18) )
list.append( Mathima("Theoria Shmaton kai Systhmaton","https://upatras-gr.zoom.us/j/3189977126?pwd=a05FV3hrYnZhTDVGY3ptVE5nNElIdz09","Wednesday",18,21) )
list.append( Mathima("Domes Dedomenon","https://upatras-gr.zoom.us/j/92396242820?pwd=Tlk1QmNjYks3ZmFJc2UwVEtHTE0yUT09","Thursday",15,17) )
list.append( Mathima("Sygxrona Themata Arxitektonikhs","https://upatras-gr.zoom.us/j/95298846407?pwd=ZEMrT1QzdkozK0lmeDcrUC9xRkRodz09#success","Thursday",17,19) )
list.append( Mathima("Psifiaka Hlektronika","https://teams.microsoft.com/l/team/19%3a5050395caf7f46f787e9a1943fcd842b%40thread.tacv2/conversations?groupId=a4a5fb9f-8233-4249-8d30-ad570390d224&tenantId=5a52ab58-42d0-4bb4-b3fc-713dd6822d20","Thursday",19,21) )

# 2 mathimata 2ou eksaminou pou xrostao
list.append( Mathima("Grammiki Algebra","https://upatras-gr.zoom.us/j/98551196932?pwd=K0FWY1NUSG94SWRmOWQ2OXB0dmNpdz09","Monday",12,14) )
list.append( Mathima("Grammiki Algebra","https://upatras-gr.zoom.us/j/98551196932?pwd=K0FWY1NUSG94SWRmOWQ2OXB0dmNpdz09","Wednesday",9,12) )
list.append( Mathima("Logikh Sxediash 2","https://upatras-gr.zoom.us/j/7170553726?pwd=aTVsMmJtVGY2RExCS0dKdWlmekdiQT09","Friday",9,12) )

# mathima epilogis
list.append( Mathima("Agglika 2","https://upatras-gr.zoom.us/j/6572548289?pwd=UXdLWXJMUnRHLzZXQTlkalFjWlN4UT09#success","Thursday",9,12) )

today_list = []

for obj in list:
    if obj.day == today :
        today_list.append(obj)

today_list.sort(key=lambda x: x.starting_hour, reverse=False)

found_class = False
for obj in today_list:
    #if (obj.ending_hour < ora) :
        #today_list.pop(0)
    if (obj.starting_hour <= ora and obj.ending_hour > ora) :
        print("Exeis '" + obj.name + "'   (" + str(obj.starting_hour) + ' - ' + str(obj.ending_hour) + '). Anoigo to link : ')
        print(obj.link)
        webbrowser.open(obj.link, new = 2)
        found_class = True
        break

if found_class == False :
    print("Den exeis Mathima Tora.")
    if today_list:
      print("Shmerino programma : ")
      for obj in today_list:
        print("||" + obj.name + "|| --> " + str(obj.starting_hour) + " - " + str(obj.ending_hour) + " <-- ")
      print("Next class in " + str(today_list[0].starting_hour-ora-1) + " ores kai " + str(60 - datetime.datetime.now().minute) + " lepta...")
    elif not today_list:
      print("Den exeis allo mathima shmera")

input("Press Enter to close the program.")
