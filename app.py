import json
import os
import sys
from datetime import datetime

from flask import Flask
import assemblyai as aai
import pika

from model.analysis import Analysis
from model.recording import Recording

app = Flask(__name__)

aai.settings.api_key = "17d12fa0b5fd4ead94732c894bca89f8"

# Set up RabbitMQ connection parameters
rabbitmq_host = 'localhost'
rabbitmq_exchange = 'amq.direct'
rabbitmq_queue = 'stt-queue'
rabbitmq_response_queue = 'stt-response'


def send(body):
    connection_response = pika.BlockingConnection(
        pika.ConnectionParameters(host=rabbitmq_host))
    channel_response = connection_response.channel()

    channel_response.queue_declare(queue=rabbitmq_response_queue, durable=True)

    channel_response.basic_publish(exchange=rabbitmq_exchange, routing_key='stt-response', body=body)


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=rabbitmq_host))
    channel = connection.channel()
    channel.exchange_declare(exchange=rabbitmq_exchange, durable=True)
    channel.queue_declare(queue=rabbitmq_queue, durable=True)

    def callback(ch, method, properties, body):
        print(body)
        recording = Recording(**json.loads(body))
        # transcriber = aai.Transcriber()
        # transcript = transcriber.transcribe(recording.recordingURI)
        analysis_obj = Analysis(0, recording.id, "Test title", "", datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
                                "transcript.text")
        send(json.dumps(analysis_obj.to_dict()))

    channel.basic_consume(queue=rabbitmq_queue, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
