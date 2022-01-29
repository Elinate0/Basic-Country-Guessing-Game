from countryinfo import CountryInfo
import random
import time
import requests
import json

## Country list from json
countryList = requests.get(f'https://gist.githubusercontent.com/Elinate0/41d8e95b0cdadb97b14de6d332bfdd46/raw/e8d6d1d29ed7a954e2d85487176483257096a944/countries').text ## If you have own json file you need to write here
countries = json.loads(countryList)
## Country list from json


def start():
    """ Random country selection function """
    gameCountry(random.choice(countries)["name"])

def gameCountry(country):
    """ That's where the game starts """
    baseInformation = CountryInfo(f'{country}')
    print("Give me a second i need to choose a country,")
    time.sleep(4)
    print("Ok i chose country,")
    time.sleep(2)
    print("I will give you 2 tips about the country I chose,")
    time.sleep(2)
    print("The capital of my chosen country is {0} and the region of the country I have chosen is located in {1}"
          .format(baseInformation.info()["capital"], baseInformation.region()))
    print("Remember, you have 3 guesses.")
    answer = False
    hintCount = 3
    answerCount = 0
    while answer == False:
        print("Do you have any guesses or want a hint?")
        userInput = input("User: ")
        if answerCount == 3:
            print("You lost!")
            print("Do you want to play again?")
            userInput = input("User: ")
            if userInput.lower() == "yes" or userInput.lower() == "ok" or userInput.lower() == "okey":
                start()
            else:
                print("Then goodbye...")
                quit()
        if userInput.lower() == country.lower():
            print("Right! you win!")
            answerCount = 0
            print("Do you want to play again?")
            userInput = input("User: ")
            if userInput.lower() == "yes" or userInput.lower() == "ok" or userInput.lower() == "okey":
                start()
            else:
                print("Then goodbye...")
                quit()
        if userInput.lower() == "yes" or userInput.lower() == "okey" or userInput.lower() == "ok" :
            hintCount -=1
            if hintCount > 0:
                hint("Countries", country)
            else:
                print("Sorry, you're out of tips.")
        elif userInput.lower() != country.lower():
            print("Wrong! try again")
            answerCount +=1
            print("number of attempts: {}".format(answerCount))

def hint(category, country = None):
    """ Hint for user """
    if category == "Countries":
        baseInformation = CountryInfo(f'{country}')
        hintsInfo = [baseInformation.borders(), baseInformation.subregion(), baseInformation.languages(), baseInformation.population()]
        choosenHint = random.choice(hintsInfo)
        if choosenHint == hintsInfo[0]:
            print("The neighbors of my chosen country are: "+ str(baseInformation.borders()))
            pass
        elif choosenHint == hintsInfo[1]:
            print("The subregion of the country of my choice: "+ str(baseInformation.subregion()))
            pass
        elif choosenHint == hintsInfo[2]:
            print("Languages spoken in my chosen country: "+ str(baseInformation.languages()))
            pass
        elif choosenHint == hintsInfo[3]:
            print("The population of my chosen country: "+ str(baseInformation.population()))
            pass

print("Hi, welcome to the country guessing game!")
time.sleep(0.80)
start()
