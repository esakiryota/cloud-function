import random

class CreateMessage:
    length = [1000, 2000, 3000, 4000, 5000]
    
    def create_title_message(self, category):
        title_msg = category + "の小説のタイトルを1つ生成して。"
        return title_msg
    
    def create_content_message(self, title):
        content_msg =  "タイトルが" + title + "の小説を" + str(random.choice(self.length)) + "字以内で書いて。" 
        return content_msg