# training with the help of list

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#creation of new chat bot
bot =ChatBot("Pawan")

trainer=ListTrainer(bot)

trainer.train([
    "Hi",
    "Hello",
    "Who are you ?",
    "I am sharma ",
    "Are you abnormal ?",
    "Yes I'm.."
])

while True:
    query=input("You : ")
    response=bot.get_response(query)
    print(response)