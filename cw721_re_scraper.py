import requests
import pandas as pd
import time
import cloudscraper

def random():
    scraper = cloudscraper.create_scraper()
    csv = r'500k_1.csv'
    csv_df = pd.read_csv(csv)
    for index, row in csv_df.iterrows():
        post_csv = pd.read_csv(r'500k_1_post.csv')
        items = scraper.get(f"https://randomearth.io/api/items?user_addr={row['address']}&collection_addr=&page=1").json().get('items')
        try:
            #print(len(items[0]))
            items = len(items[0])
            if items != 0:
                post = pd.DataFrame(row).T
                pd.concat([post_csv, post], ignore_index=True).to_csv('500k_1_post.csv', index = False)
            print(f"Have added {row['address']}")
        except:
            pass

        csv_df.drop([index], inplace=True)
        csv_df.to_csv(csv, index=False)    
        time.sleep(.5)

while 500000 - len(pd.read_csv('')) < 500000:
    try:
        random()
    except Exception as e:
        print()
        print(e)
        print()
        time.sleep(60)
    