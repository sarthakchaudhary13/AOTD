# main script for the application, Will change in future when structure of project become complex
import json
import os
import random
from datetime import datetime

from sapera.settings import BASE_DIR


def update_data_info():
    """
    This function will run the updater.sh script
    in the scraper package, to update the list of algorithm in data/

    :return:
    """
    print(BASE_DIR)
    if os.name == 'nt':
        os.system("{x}\\sapera\\scraper\\updater.cmd {x}".format(
            x = BASE_DIR)) #calling updater.cmd
    else:
        os.system("bash {x}/sapera/scraper/updater.sh {x}".format(
            x=BASE_DIR))  # calling the updater.sh

    with open(BASE_DIR + "/sapera/scraper/status.txt", "r") as status:
        print(status.read())


def download_data():
    """
    This function will download the additional algorithmns
    which will be added in the list of algorithms

    :return:
    """
    pass


def random_generator():
    info_file_name = BASE_DIR + "/data/.list-of-algorithms.json"
    today_algo_file = BASE_DIR + "/data/today.json"

    with open(info_file_name, "r") as f:
        data = json.load(f)

    topics = list(data.keys())

    topic = data[random.choice(topics)]
    algo = random.choice(topic)

    with open(today_algo_file,"r+") as t:
        try:
            today_algo = json.load(t)

            if datetime.today().strftime('%Y-%m-%d') == today_algo['date']:
                return today_algo['algo']
            else:
                today_algo = {
                    'date':datetime.today().strftime('%Y-%m-%d'),
                    'algo':algo
                }
                t.seek(0)
                t.write(json.dumps(today_algo,indent=4))
                return algo
        except:
            today_algo = {
                'date':datetime.today().strftime('%Y-%m-%d'),
                'algo':algo
            }
            t.seek(0)
            t.write(json.dumps(today_algo,indent=4))
            return algo
