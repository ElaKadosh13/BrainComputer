import pika


class Mq:
    def __init__(self, address):
        self.channel = None
        self.host, self.port = self.check_address(address)
        print(self.host)
        print(self.port)

    def check_address(self, address):
        split_addr = address.replace("/", "").split(":")
        if len(split_addr) != 3:
            raise Exception("invalid rabbitmq url")
        if split_addr[0] != 'rabbitmq':
            raise Exception("invalid rabbitmq url")
        return split_addr[1:]


    def create_queue(self, name, type):
        print("creting queue")
        connection_parameters = pika.ConnectionParameters(self.host, self.port)
        print(connection_parameters)
        print(pika.BlockingConnection(connection_parameters))
        connection = pika.BlockingConnection(connection_parameters)
        print("connected mq")
        self.channel = connection.channel()
        self.channel.exchange_declare(exchange=name, exchange_type=type)

    def consume_queue(self, name, callback, key=''):
        q = self.channel.queue_declare(queue='', exclusive=True)
        q_name = q.method.queue
        if key == '':
            self.channel.queue_bind(exchange=name, queue=q_name, routing_key=key)
        else:
            for k in key:
                self.channel.queue_bind(exchange=name, queue=q_name, routing_key=k)
        self.channel.basic_consume(queue=q_name, on_message_callback=callback, auto_ack=True)
        self.channel.start_consuming()

    def send_to_queue(self, name, body, key=''):
        print("sending to queue")
        self.channel.basic_publish(exchange=name, routing_key=key, body=body)

    def send_to_basic_queue(self, body):
        self.send_to_queue('queue', body)