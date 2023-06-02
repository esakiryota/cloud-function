import requests
import random
import json
import os
from dotenv import load_dotenv
import pprint 

class Connection:
    load_dotenv()

    api_url = os.getenv("NEXT_API_URL")
    word_len = [1000, 2000, 3000, 4000, 5000]
    
    def api_connection(self):
        try:
            url = self.api_url
            return url
        except Exception as e:
            print(e)
            return e
    def get_chatgpt_account(self):
        try:
            url = self.api_url + "users/chatgpt/"
            res = requests.get(url,verify=False)
            pk = res.json()["pk"]
            id = res.json()["id"]
            return [pk, id]
        except Exception as e:
            print(e)
            return e
    
    def get_categories(self):
        try:
            url = self.api_url + "categories/get"
            res = requests.get(url,verify=False)
            return res.json()
        except Exception as e:
            print(e)
            return e
    
    def get_words_len(self):
        len = str(random.choice(self.sword_len))
        return len
    
    def post_novel(self, title, category, content, user_id, user_pk):
        url = self.api_url + "novels/create/"
        novel_values = { "title": title, "user_pk": user_pk, "user_id": user_id, "content": content, "category_pk": category["pk"] }
        try:
            # data = 
            res = requests.post(url, data=json.dumps(novel_values), verify=False)
            return res
        except Exception as e:
            print(e)
            return e

    
