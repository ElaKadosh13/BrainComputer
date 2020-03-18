import pika


class Mq:
    def __init__(self):
        self.channel = None

    def create_queue(self, name):
        connection_parameters = pika.ConnectionParameters(
            'localhost')  # 'rabbitmq://127.0.0.1', '5672') #todo 'rabbitmq://127.0.0.1:5672/'
        connection = pika.BlockingConnection(connection_parameters)
        self.channel = connection.channel()
        self.channel.exchange_declare(exchange=name, exchange_type='fanout')

    def consume_queue(self, name, callback):
        q = self.channel.queue_declare(queue='', exclusive=True)
        q_name = q.method.queue
        self.channel.queue_bind(exchange=name, queue=q_name)
        self.channel.basic_consume(queue=q_name, on_message_callback=callback, auto_ack=True)
        self.channel.start_consuming()

    def send_to_queue(self, name, body, parser_key):
        print("sending to queue")
        self.channel.basic_publish(exchange=name, routing_key=parser_key, body=body)
