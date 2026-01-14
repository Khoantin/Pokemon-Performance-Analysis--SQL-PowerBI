from bs4 import BeautifulSoup
import requests
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import pymysql


def scrape():
    total_count = 1025
    current_count = 0

    url = 'https://pokemondb.net/'
    table_url = 'pokedex/all'
    poke_data = []
    site = requests.get(url + table_url)
    soup = BeautifulSoup(site.text, "html.parser")
    poke_urls = []

    #Loops through each element(pokemon) in the Tbody and appends URL.
    for i in soup.select("td.cell-name a"):
        poke_urls.append(i["href"])
    #Visits each elements URL and records its statistics and value.
    
    for poke_url in poke_urls:
        poke_site = requests.get(url + poke_url)
        psoup = BeautifulSoup(poke_site.text,"html.parser")
        tbody = psoup.find("tbody")
        #---General Stats--
        name = psoup.find("h1").text
        generation = psoup.find("p").find("abbr").text.replace("Generation ","")
        id = tbody.find("strong").text
        weight = tbody.find("th", string = "Weight").find_next("td").text
        weight = weight.split("(")[1].replace("lbs)","").strip() 
        height = tbody.find("th", string = "Height").find_next("td").text
        height = height.split("m")[0].strip() 
        hidden_abl = tbody.find("th", string = "Abilities").find_next("td").find("small")

        training_tbody =  psoup.find("h2", string = "Training").find_next("table").find("tbody")
        catch_rate = training_tbody.find("th", string = "Catch rate").find_next("td").text.split(" ")[0].strip()
        
        #grabbing image.
        img_url = psoup.find("div", class_="sv-tabs-panel-list").find("img")["src"]

        if hidden_abl:
            hidden_abl = True
        else: hidden_abl = False

        types = tbody.find_all("a", class_="type-icon")
        type2 = None
        if len(types) > 1: #some Pokemon(elements) dont have 2 types.
            type2 = types[1].text
        type1 = types[0].text
        
        #---Combat Stats---
        cstats = [] # a list of stats for each pokemon, indexing through this gives the specific stats
        #Ex: hp = 0, atk = 1
        stats_th = psoup.find("div",class_="resp-scroll").find("tbody").find_all("tr")
        for s in stats_th:
            cstats.append(s.find("td").string)

        #adds all of the pokemon into the set.
        poke_data.append({
            "Id": id,
            "Name": name,
            "Type1":type1,
            "Type2": type2,
            "Weight":weight,
            "Height":height,
            "Hp":cstats[0],
            "Attack":cstats[1],
            "Defense":cstats[2],
            "Sp_Attack":cstats[3],
            "Sp_Defense":cstats[4],
            "Speed":cstats[5],
            "Hidden_ability": hidden_abl,
            "Generation": generation,
            "Catch_rate": catch_rate,
            "img_url": img_url

        })
        current_count += 1
        percentage = str(current_count / total_count)[:5]
        print(f"{percentage}% completed, added:{name}")
    df = pd.DataFrame(poke_data)
    df = df.drop_duplicates(subset="Name",keep="first")
    return df
        
def Sql_upload(df):
    #uploads image to sql server, at localhost with pass= password
    
    print("Data scraping Completed. Uploading to sql server now.")
    
    con_string = 'mysql+pymysql://root:password@localhost/pokedata'
    print(f"Connecting at:{con_string}")
    engine = create_engine(con_string)

    df.to_sql('poke_table',engine,if_exists='replace',index = False)
    print("Data Transfer success!")

if __name__ == "__main__":
    Database = scrape()
    Sql_upload(Database)
    
