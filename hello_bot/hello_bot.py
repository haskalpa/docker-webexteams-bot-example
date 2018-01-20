#!/usr/bin/env python
#  -*- coding: utf-8 -*-

# 3rd party imports ------------------------------------------------------------
from flask import Flask, request
from ciscosparkapi import CiscoSparkAPI, Webhook

# local imports ----------------------------------------------------------------
from helpers import (read_yaml_data,
                     get_ngrok_url,
                     find_webhook_by_name,
                     delete_webhook, create_webhook)


flask_app = Flask(__name__)
spark_api = None


@flask_app.route('/sparkwebhook', methods=['POST'])
def sparkwebhook():
    if request.method == 'POST':

        json_data = request.json
        print("\n")
        print("WEBHOOK POST RECEIVED:")
        print(json_data)
        print("\n")

        webhook_obj = Webhook(json_data)
        # Details of the message created
        room = spark_api.rooms.get(webhook_obj.data.roomId)
        message = spark_api.messages.get(webhook_obj.data.id)
        person = spark_api.people.get(message.personId)
        email = person.emails[0]

        print("NEW MESSAGE IN ROOM '{}'".format(room.title))
        print("FROM '{}'".format(person.displayName))
        print("MESSAGE '{}'\n".format(message.text))

        # Message was sent by the bot, do not respond.
        # At the moment there is no way to filter this out, there will be in the future
        me = spark_api.people.me()
        if message.personId == me.id:
            return 'OK'
        else:
            spark_api.messages.create(room.id, text='hello')
    else:
        print('received none post request, not handled!')


if __name__ == '__main__':
    config = read_yaml_data('/opt/config/config.yaml')['hello_bot']
    spark_api = CiscoSparkAPI(access_token=config['spark_access_token'])

    ngrok_url = get_ngrok_url()
    webhook_name = 'hello-bot-wb-hook'
    dev_webhook = find_webhook_by_name(spark_api, webhook_name)
    if dev_webhook:
        delete_webhook(spark_api, dev_webhook)
    create_webhook(spark_api, webhook_name, ngrok_url + '/sparkwebhook')

    flask_app.run(host='0.0.0.0', port=5000)
