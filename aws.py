import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from tkinter import messagebox

ENDPOINT = "a966pdrxzoia6-ats.iot.us-east-1.amazonaws.com"
ROOT_PATH ="/Users/sergekhvan/Projects/capstone/awsiot/root-ca.pem"
PRIVATE_PATH ="/Users/sergekhvan/Projects/capstone/awsiot/private.pem.key"
CERTIFICATE_PATH="/Users/sergekhvan/Projects/capstone/awsiot/certificate.pem.crt"

class AWSclient:
    def __init__(client):
        client.payload = 100
        client.myMQTTClient = AWSIoTMQTTClient("ClientID ") #random key , if another connection using the same key is
        client.myMQTTClient.configureEndpoint(ENDPOINT, 8883)
        client.myMQTTClient.configureCredentials(ROOT_PATH, PRIVATE_PATH,CERTIFICATE_PATH)


        client.myMQTTClient.configureOfflinePublishQueueing( -1 ) # Infinite offline Publish queueing
        client.myMQTTClient.configureDrainingFrequency( 2 )# Draining : 2 Hz
        client.myMQTTClient.configureConnectDisconnectTimeout( 10 )# 10 sec
        client.myMQTTClient.configureMQTTOperationTimeout( 5 )# 5 sec
        print(' Initiating IoT Core Topic ... ')
        client.myMQTTClient.connect( )
        print("connected")
        pass
    
    def receive_mes(client, self, param, packet) :
        client.payload = packet.payload
        print(client.payload)
        messagebox.showinfo(title="Doctor's comments", message=f"{client.payload}")
        
    
    def aws_sub(client,topic): 
        client.myMQTTClient.subscribe(topic, 1, client.receive_mes)

            
    def aws_pub(client,topic,line):  
        print(f"Publishing to {topic}")      
        client.myMQTTClient.publish(
                topic=topic,
                QoS=1,
                payload=line
                )
                

            