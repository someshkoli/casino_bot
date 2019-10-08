import sys,os
import time
import telepot
from web3 import Web3
from telepot.loop import MessageLoop
import json
from telepot.namedtuple import KeyboardButton,ReplyKeyboardMarkup
markup = ReplyKeyboardMarkup(keyboard=[
                                    [KeyboardButton(text="Deposite"), KeyboardButton(text='Check Balance'),KeyboardButton(text="withdrawl")],
                                    [KeyboardButton(text="Coins available"), KeyboardButton(text='Request New Coin')],
                                    [KeyboardButton(text="Disclaimer"), KeyboardButton(text='Help')],
                                ])


# Message handler
def handle(msg):
    content_type,chat_type,chat_id= telepot.glance(msg)
    # print(content_type,chat_id,chat_type)
    bot.sendMessage (chat_id, str("Hi select from any one of the following options ."), reply_markup=markup)
    print(msg['text'])
    if msg['text']=='Deposite':
        deposite(msg)
        return
    if msg['text']=='Check Balance':
        getBalance(msg)
        return
    if msg['text']=='Withdrawl':
        withdrawl(msg)
        return
    if msg['text']=='coins available':
        printCoinsAvailable(msg)
        return
    if msg['text']=='Desclaimer':
        printDesclaimer(msg)
        return
    if msg['text']=='Request new coin':
        newCoinRequest(msg)
        return
    if msg['text']=='Help':
        printHelp(msg)
        return
    if msg["tip"]=="/Tip":
        sendTip()    
        return


# functions to be handled
def printHelp(msg):
    content_type,chat_type,chat_id= telepot.glance(msg)
    bot.sendMessage (chat_id, str("Help text."), reply_markup=markup)
    return 

def printCoinsAvailable(msg):
    content_type,chat_type,chat_id= telepot.glance(msg)
    bot.sendMessage(chat_id,str("eth,casino,bitcoin etc"),reply_markup=markup)

def newCoinRequest(msg):
    print("new coin req called")

def printDesclaimer(msg):
    content_type,chat_type,chat_id= telepot.glance(msg)
    bot.sendMessage(chat_id,str("desclaimer text"),reply_markup=markup)

def deposite(msg):
    print("deposite called, is connected ")

    print(web3.isConnected())

def getBalance(msg):
    print("getBalance called, is connected ")
    account="0x719506f109df260057De122614d537176925e2e2"
    print(web3.isConnected())
    balance =web3.fromWei(web3.eth.getBalance(account),'ether')

def withdrawl(msg):
    print("withdrawl called, is connected ")
    print(web3.isConnected())

def sendTip(msg):
    print("sending tips,is connected ")
    print(web3.isConnected())

TOKEN=os.environ.get('BOT_TOKEN')
infura_url=os.environ.get('ROPSTEN_URL')
bot = telepot.Bot(TOKEN)
web3 = Web3(Web3.HTTPProvider(infura_url))
with open("./build/contract_abi.json") as f:
    info_json = json.load(f)
abi = info_json
with open("./build/contract_bytecode.json") as f:
    info_json = json.load(f)
bytecode = info_json
contract_adress=os.environ.get("CONTRACT_ADDRESS")
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')
# Keep the program running.
while 1:
    time.sleep(10)
