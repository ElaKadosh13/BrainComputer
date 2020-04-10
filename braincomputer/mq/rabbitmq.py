import pika


class Rabbitmq:
    def __init__(self, host, port):
        self.channel = None
        self.host = host
        self.port = port

    def create_queue(self, name, type):
        connection_parameters = pika.ConnectionParameters(self.host, self.port)
        print(connection_parameters)
        print(pika.BlockingConnection(connection_parameters))
        connection = pika.BlockingConnection(connection_parameters)
        self.channel = connection.channel()
        self.channel.exchange_declare(exchange=name, exchange_type=type)

    def consume_from_queue(self, name, callback, key=''):
        q = self.channel.queue_declare(queue='', exclusive=True)
        q_name = q.method.queue
        if key == '':
            self.channel.queue_bind(exchange=name, queue=q_name, routing_key=key)
        else:
            for k in key:
                self.channel.queue_bind(exchange=name, queue=q_name, routing_key=k)
        self.channel.basic_consume(queue=q_name, on_message_callback=callback, auto_ack=True)
        self.channel.start_consuming()

    def send_to_queue(self, body, name='queue', key=''):
        self.channel.basic_publish(exchange=name, routing_key=key, body=body)

    def close_queue(self):
        self.channel.close()
