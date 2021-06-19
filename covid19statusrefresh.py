import requests , subprocess , socket , time , os , json
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

    hpb = json.loads(alldata)
    data = hpb['data']


    #getting local data location
    Ltotal = data['local_total_cases'] 
    Ldeath = data['local_deaths'] 
    Lrecov = data['local_recovered'] 
    Lnewd = data['local_new_deaths'] 
    #Getting Global data location
    Gtotal = data["global_total_cases"]
    Gdeath = data["global_deaths"]
    Grecov = data["global_recovered"]
    Gnewd = data['global_new_deaths'] 
    updateTD = data["update_date_time"]  
  
  
    print("-----COVID19 STATUS----\n")
 
    print(Fore.LIGHTCYAN_EX + "[+] Sri Lanka Status : \n")
    print(Fore.LIGHTGREEN_EX + "Local Total Cases :",Ltotal)
    print("Local Deaths :",Ldeath)
    print("Local Recovered :",Lrecov)
    print("Local New Deths :",Lnewd)

    print("")
    print(Fore.LIGHTCYAN_EX + "[+] Global Status : \n")
    print(Fore.LIGHTGREEN_EX + "Global Total Cases :",Gtotal)
    print("Global Deaths :",Gdeath)
    print("Global Recovered :",Grecov)
    print("Global New Deths :",Gnewd)
    print(Fore.LIGHTCYAN_EX + "\nLast Updated :",updateTD)
    print("\nRefresh Rate : 1 Minute")
  else:
    
      print("Error ! Unable to connect to host")
      print("Status code : ",rcode)

  time.sleep(60)
  os.system('cls')

input("\nExit >")
