# Python3-web-scrapping-6-minutes-english
python3 6 minutes english web scrapping

### App Features ###

    * Scrap english materials from 6 minute english website.
    
    * Used panda, requests and BeautifulSoup
    
    * Upload scrapped data to firebase with the instruction in project folder 'firebase-import'

This app is associated with this project [here][src]

[src]: https://github.com/ultralabed/ReactNative-6-minutes-english-App

```
# python version 3.6
# node version 6.9
pip3 install pandas==0.19.2 requests==2.13.0 beautifulsoup4==4.5.3
python3 myscript.py
python3 csv_to_json.py
firebase-import --database_url https://minutes-english.firebaseio.com/ --path / --json ../data.json
```