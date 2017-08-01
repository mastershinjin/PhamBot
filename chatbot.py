from chatterbot import ChatBot

chatbot = ChatBot(
    'PhamBot',
    trainer='chatterbot.trainers.ListTrainer',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    database='./phambot.sqlite3'
)

def parseList():
    dList = list()
    with open("phamquotes.txt", "r") as f:
        
        for entry in f.read().split("@"):
            entryList = list()
            for line in entry.split("\n"):
                if(line.strip() != ""):
                    entryList.append(line.strip())

            # train
            chatbot.train(entryList)

#parseList()

while True:
    try:
        bot_input = chatbot.get_response(None)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
