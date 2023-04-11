from os import getenv,system
import requests
from dotenv import load_dotenv
import json
from pprint import pprint
load_dotenv()

USER_URL = getenv('URL')

def get_request(url):
    response = requests.get(url)

    if response.status_code ==200:
        data = response.json()
        return data
    else:
        return f"Plohoi zapros: {response.status_code}"
    
def random_users(random_url=USER_URL):

    data = get_request(random_url)
    # with open('core/json/users.json', 'w', encoding="UTF-8") as json_file:
    #     json.dump(data, json_file, indent=4, ensure_ascii=False)
    # pprint(data)
    data = data['results'][0]
    information = f"""
Foto : {data['picture']['large']}    
FIO : {data['name']['title']}{data['name']['first']}{data['name']['last']}
Data rozhdeniya : {data['dob']['date']}
Vozrast : {data['dob']['age']}
Pol: {data['gender']}
Nacionalnost :{data['nat']}
Strana : {data['location']['country']}
Gorod : {data['location']['city']}
Region: {data['location']['state']}
Mestopolozhenie : {data['location']['coordinates']['latitude']}, {data['location']['coordinates']['longitude']} 
Dom nomer : {data['phone']}
Mobilny nomer : {data['cell']}

Elektr pochta : {data['email']}
Polzovatel imya : {data['login']['username']}
Parol : {data['login']['password']}
Data registracii : {data['registered']['date']}
"""
    return information
   
print(random_users(USER_URL)    )
    