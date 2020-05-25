# main script for the application, Will change in future when structure of project become complex
import json
import os
import random

from sapera.settings import BASE_DIR


def update_data_info():
    """
    This function will run the updater.sh script
    in the scraper package, to update the list of algorithm in data/

    :return:
    """
    os.system("bash {x}/sapera/scraper/updater.sh {x}".format(
        x=BASE_DIR))  # calling the updater.sh


def download_data():
    """
    This function will download the additional algorithmns
    which will be added in the list of algorithms

    :return:
    """
    pass
    # Work in Progress


def random_generator():
    info_file_name = BASE_DIR + "/data/.list-of-algorithms.json"

    with open(info_file_name, "r") as f:
        data = json.load(f)

    topics = list(data.keys())

    topic = data[random.choice(topics)]
    algo = random.choice(topic)

    return algo
