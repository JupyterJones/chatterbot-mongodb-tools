#!/home/jack/miniconda3/envs/deep/bin/python
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging
import bson

# Uncomment the following line to enable verbose logging
# logging.basicConfig(level=logging.INFO)

# Create a new ChatBot instance
Botman = ChatBot('Botman',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=['chatterbot.logic.BestMatch'],
    filters=['chatterbot.filters.RepetitiveResponseFilter'],
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    database_uri='mongodb://localhost:27017/super-chatbot'
)
trainer = ChatterBotCorpusTrainer(Botman)
    
trainer.export_for_training('GIGANTIC.json')


print('Type something to begin...')

while True:
    try:
        user_input = input()
        if user_input=="quit":
            break
        bot_response = Botman.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
#chatbot.get_response("Hello, how are you today?")