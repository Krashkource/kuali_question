import requests
import json

SWAPI_URL = 'http://swapi.co/api'
STARSHIPS = 'starships'
PEOPLE = 'people'

def print_starships_and_owners():
    query = "{0}/{1}".format(SWAPI_URL, PEOPLE)
    people = {}
    while True:
        response = requests.get(query)
        json_data = json.loads(response.content.decode('utf-8'))
        for resource in json_data['results']:
            people[resource['url']] = resource['name']
        if not json_data['next']:
            break
        query = json_data['next']

    query = "{0}/{1}".format(SWAPI_URL, STARSHIPS)
    while True:
        response = requests.get(query)
        json_data = json.loads(response.content.decode('utf-8'))
        for resource in json_data['results']:
            print(resource['name'])
            for owner in resource['pilots']:
                print(u'  {0}'.format(people[owner]))
        if not json_data['next']:
            break
        query = json_data['next']

if __name__ == "__main__":
    print_starships_and_owners()