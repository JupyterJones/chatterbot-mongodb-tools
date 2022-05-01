#app_key=YazCRIfWX4VICiRCOiph08jDL
#app_secret=QOkLHou6NMwkghSHjMFXMdffQKJlDzttKtP6uBCcZ4VlQtvJyc
#oauth_token=296906916-AWggjhqpEWIS7EzXXhc2pOPBeCVJczpOm11cQGIf
#oauth_token_secret=zFrCiyaPt8gCBVVs1bLCmdCSyQQ3DKxT5wHJq2tOu2AMj
GITTER = {
    'name':'GitterBot',
    'ROOM': 'errbotio/errbot',
    'API_TOKEN': '7af0a02fc3c43281482f60a925d7303acfa79990'
}



TWITTER = {
    "CONSUMER_KEY": "YazCRIfWX4VICiRCOiph08jDL",
    "CONSUMER_SECRET": "QOkLHou6NMwkghSHjMFXMdffQKJlDzttKtP6uBCcZ4VlQtvJyc",
    "ACCESS_TOKEN": "296906916-AWggjhqpEWIS7EzXXhc2pOPBeCVJczpOm11cQGIf",
    "ACCESS_TOKEN_SECRET": "zFrCiyaPt8gCBVVs1bLCmdCSyQQ3DKxT5wHJq2tOu2AMj"
}


ChatBot = {
    'name': 'Gohart',
    'logic_adapters': [
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ],
    'trainer': 'chatterbot.trainers.ChatterBotCorpusTrainer',
    'training_data': [
         'chatterbot.corpus.english.greetings'
    ]
}

