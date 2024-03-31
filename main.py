import time
import requests
import json

def data_scraping():
    initial_url = "https://steamcommunity.com/market/search/render/?query=&l=english&start=0&count=0&search_descriptions=0&sort_column=price&sort_dir=asc&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_Tournament%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&category_730_Weapon%5B%5D=any&appid=730&norender=1"
    total_count = 0

    # Get the total number of items
    # Did it this way so it can work with any number of items - even if there are new ones added
    while total_count == 0:
        response = requests.get(initial_url)
        data = json.loads(response.text)
        total_count = data['total_count']
        print(total_count)
        time.sleep(5)

    # Calculate the number of searches required to get all the data
    # There is limit of 100 items per search and because the price can change between searches, there is a 5 item overlap between searches
    number_of_searches = int((total_count-1) / 95)+1
    results = []
    for search in range(number_of_searches):
        got_data = False
        while not got_data:
            url = f"https://steamcommunity.com/market/search/render/?query=&l=english&start={search*95}&count=100&search_descriptions=0&sort_column=price&sort_dir=asc&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_Tournament%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&category_730_Weapon%5B%5D=any&appid=730&norender=1"
            response = requests.get(url)
            data = json.loads(response.text)
            if data['total_count'] > 0:
                got_data = True
                results.append(data['results'])
                print(f"Search {search} done")
            time.sleep(10)
    #print(results)

    # Combine the data to one list and create a dictionary for the data
    combined_data = sum(results, [])
    result_dict = {}

    # Iterate over the combined list
    # Necessary because the data was overlapping and there is no need to save all the columns just the ones we need
    for data in combined_data:
        result_dict[data['name']] = {'sell_price_text': data['sell_price_text'], 'sell_listings': data['sell_listings'], 'hash_name': data['hash_name'], 'sale_price_text': data['sale_price_text']}

    # for key in result_dict:
    #     print(key, result_dict[key])
    #     print("\n")

    # save data to file
    with open('data.txt', 'w') as convert_file:
        convert_file.write(json.dumps(result_dict))

def main():
    with open('data.txt', 'r') as file:
        data = json.load(file)

    print(data)

if __name__ == "__main__":
    data_scraping()
    main()

