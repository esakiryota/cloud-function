import openai
import os
from dotenv import load_dotenv
import random
from connection import Connection 
from createMessage import CreateMessage
import functions_framework

load_dotenv()

openai.api_key = os.environ['API_KEY']

@functions_framework.http
def main():
    connection = Connection()
    user_pk = connection.get_chatgpt_account()[0]
    user_id = connection.get_chatgpt_account()[1]
    create_message = CreateMessage()
    categories = connection.get_categories()
    category = random.choice(categories)
    title_msg = create_message.create_title_message(category["name"])
    print("titlemsg")
    response1 = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                {'role': 'user', 'content': title_msg},
                ],
                temperature=1,
                )
    title = response1.choices[0].message.content
    content_msg =  create_message.create_content_message(title)
    print("content_msg")
    response2 = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                {'role': 'user', 'content': content_msg},
                ],
                temperature=1,
                )
    print("content")
    content = response2.choices[0].message.content
    print(content)
    res = connection.post_novel(title, category, content, user_id, user_pk)
    return "job done"
