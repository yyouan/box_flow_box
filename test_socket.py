import websocket

#收到server傳來的message的callback
def onMessage(ws, msg):
    print("收到了從server傳來的message：" + msg)

#與server建立連線後的callback
def onOpen(ws):
    sendMessage = '安安我是python'
    ws.send(sendMessage)

#server的HOST
HOST = 'ws://127.0.0.1:12345'

#與server約定好的protocol server端也要設定
SUBPROTOCOLS = ['echo-protocol']

#建立websocket
ws = websocket.WebSocketApp(HOST, subprotocols = SUBPROTOCOLS, on_open = onOpen, on_message = onMessage)

#一直執行
ws.run_forever()