import requests
from apiKey import key
import requests
import json

# Functions Below

# Gets users current rank by origin name
def getRank(name):
    # Request using key and supplied name.
    callRank = requests.get(
        f"https://api.mozambiquehe.re/bridge?auth={key}&player={name}&platform=PC"
    ).json()
    # Current rank name
    currentRank = callRank["global"]["rank"]['rankName']
    # Current rank division (The number next to the rank, example Gold "4")
    currentDivision = callRank['global']['rank']['rankDiv']
    # Prints full rank
    print("Current rank is", currentRank,currentDivision)

# Gets users stats from supplied username
def getStat(name):
    try:
        # Request using key and supplied name.
        callLegend = requests.get(
            f"https://api.mozambiquehe.re/bridge?auth={key}&player={name}&platform=PC"
        ).json()
        # Gets current legend from the json returned by request
        currentLegend = callLegend["realtime"]["selectedLegend"]
        # Uses current legend to get data relevant to Legend that is selected
        legendStats = callLegend["legends"]["all"][currentLegend]["data"]
        print("Stats for:", str(currentLegend))
        # Loops through all items and prints all the stats names and values.
        for item in legendStats:
            print(item["name"], ":", item["value"])
    except KeyError:
        # Catches Key Errors, if they don't uses origin name it won't work and will error.
        print(name, "was not recognized, make sure you're using your origin name")

def news():
    news = requests.get(f'https://api.mozambiquehe.re/news?auth={key}').json()
    recentNews = news[0]
    print("MOST RECENT NEWS ANNOUNCEMENT")
    for item in recentNews:
        print(item + ":", recentNews[item])



if __name__ == "__main__":
    print()