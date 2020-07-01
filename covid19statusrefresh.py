import requests , subprocess , socket , time , os
from colorama import Fore , init
init()

while True:
  print(Fore.LIGHTGREEN_EX + "  _____            _     _  __   _____      _____ _        _              ")
  print(" /  __ \          (_)   | |/  | |  _  |    /  ___| |      | |             ")
  print(" | /  \/ _____   ___  __| |`| | | |_| |    \ `--.| |_ __ _| |_ _   _ ___  ")
  print(" | |    / _ \ \ / / |/ _` | | | \____ |     `--. \ __/ _` | __| | | / __| ")
  print(" | \__/\ (_) \ V /| | (_| |_| |_.___/ /    /\__/ / || (_| | |_| |_| \__ \ ")
  print("  \____/\___/ \_/ |_|\__,_|\___/\____/     \____/ \__\__,_|\__|\__,_|___/ ")
  print(Fore.LIGHTYELLOW_EX + "---------------------------------------------------------------------------")
  print(" [+] Made by GHOSTH4CK3R    [+] Data From : www.hpb.health.gov.lk \n")
  print(Fore.LIGHTGREEN_EX + "")
  try:
    ip = socket.gethostbyname("www.google.com")    
  except Exception as e:
    print("No Internet > Exitting in 10 seconds")  
    time.sleep(10)
    exit()

  #Connecting to Api 
  url = "https://www.hpb.health.gov.lk/api/get-current-statistical"
  #Get Request
  response = requests.get(url)
  rcode = response.status_code
  alldata = response.text

#Filtering by status code
  if rcode == 200 :  
      
    print("...Connected To Host...\n")

    data = alldata.replace("{"," ")
    data = data.replace("{"," ")
    #getting local data location
    Ltotal = data.find('local_total_cases') 
    Ldeath = data.find('local_death') 
    Lrecov = data.find('local_recovered') 
    #Getting Global data location
    Gtotal = data.find("global_total_cases")
    Gdeath = data.find("global_deaths")
    Grecov = data.find("global_recovered")
    updateTD = data.find("update_date_time")  
  #Getting numeric value for each data
    LocalTotal = data[(Ltotal+19):(Ltotal+25)]
    LocalDeaths = data[(Ldeath+14):(Ldeath+18)]
    LocalRecovered = data[(Lrecov+17):(Lrecov+23)]

    GlobalTotal = data[(Gtotal+20):(Gtotal+32)]
    GlobalDeaths = data[(Gdeath+15):(Gdeath+23)]
    GlobalRecovered = data[(Grecov+18):(Grecov+31)]
    UPDATEDdatetime = data[(updateTD+19):(updateTD+38)]
  #Removing last character until the variable value is numeric
    while True:
        LocalDeaths = LocalDeaths[:-1]
        if LocalDeaths.isnumeric() == True :
             break
    while True:
        LocalTotal = LocalTotal[:-1]
        if LocalTotal.isnumeric() == True :
             break
    while True:
        LocalRecovered = LocalRecovered[:-1]
        if LocalRecovered.isnumeric() == True :
             break
  
    while True:
        GlobalDeaths = GlobalDeaths[:-1]
        if GlobalDeaths.isnumeric() == True :
             break
    while True:
        GlobalTotal = GlobalTotal[:-1]
        if GlobalTotal.isnumeric() == True :
             break
    while True:
        GlobalRecovered = GlobalRecovered[:-1]
        if GlobalRecovered.isnumeric() == True :
             break
  
  
    print("-----COVID19 STATUS----\n")
 
    print(Fore.LIGHTCYAN_EX + "[+] Sri Lanka Status : \n")
    print(Fore.LIGHTGREEN_EX + "Local Infected :",LocalTotal)
    print("Local Deaths :",LocalDeaths)
    print("Local Recovered :",LocalRecovered)

    print("")
    print(Fore.LIGHTCYAN_EX + "[+] Global Status : \n")
    print(Fore.LIGHTGREEN_EX + "Global Infected :",GlobalTotal)
    print("Global Deaths :",GlobalDeaths)
    print("Global Recovered :",GlobalRecovered)
    print(Fore.LIGHTCYAN_EX + "\nLast Updated :",UPDATEDdatetime)
    print("\nRefresh Rate : 5 seconds")
  else:
      print("Error ! Unable to connect to host")
      print("Status code : ",rcode)

  time.sleep(5)
  os.system('cls')
   
input("\nExit >")