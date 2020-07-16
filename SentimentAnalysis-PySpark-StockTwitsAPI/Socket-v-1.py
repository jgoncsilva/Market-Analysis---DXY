# -*- coding : utf-8 -*-



#Import 


from stocktweepy import Stream
from stocktweepy.straming import StreamListener, Strem
from stocktweepy import OAuthHandler
import oauth2client
import socket
import json
import requests 


#Set upour credentials
consumer_key = '8ede87ef994b3e67'
consumer_secret = '22128c04dab081eea140d90a45ebf3e0025c96b6'
request_token_url = 'https://api.stocktwits.com/api/2/oauth/token'
authorize_url =  'https://api.stocktwits.com/api/2/oauth/authorize'

class TweetsListener(StreamListener):
    
    def __init__(self, csocket): #Constructor
        self.client_socket = csocket
        self.count=0
        self.limit=30
        #self.stocktweepy = stocktweepy
        
    def on_data(self, data): #Read twits and fullfill the counter
        try:
            msg = json.loads( data )
            self.count+=1
            if self.count<=self.limit:
                print(msg['text'].encode('utf-8')) #Verify the number of twits readed
                self.client_socket.send( msg['text'].encode('uft-8')) #Send messages for socket
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
    
    def on_error(self, status): #Method for know whats the reason of the error 
        print(status)
        return True

def sendData(c_socket): #define how the data will be send
    auth = OAuthHandler(consumer_key, consumer_secret) #Auth on website
    auth.set_acess_token(request_token_url, authorize_url) #Take token
    
    twits_stream = Stream(auth, TweetsListener(c_socket)) #Define the type of connection
    twits_stream.filter(track=['DXY', 'SPY']) #Define the filter to be used
    

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create objectsocket 
    host = "192.168.1.72"
    port = 4407
    s.bind((host, port)) #Bind for the port

    print("listening on port: ", port)
          
    s.listen(5)          #Time to wait for connection
    c, addr = s.accept() #Establish the conection
    
    print("Received request from " + str(addr))
          
    sendData.to_csv(c)
      
      