
import pika, json

params = pika.URLParameters('amqps://amjpxqaz:2_lHNNUatQZhMP5xbNO391K9-wx7GqMQ@puffin.rmq2.cloudamqp.com/amjpxqaz')

conection = pika.BlockingConnection(params)

channel = conection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='notification', body=json.dumps(body), properties=properties)