import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

for i in range(100_000):
    channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=f'Hello World! {i}')

print(" [x] Sent 'Hello World!'")