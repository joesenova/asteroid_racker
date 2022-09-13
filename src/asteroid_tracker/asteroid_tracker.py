"""
The Asteroid Tracker program
"""

import logging
import argparse
import requests
import json
from models import resp_models

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

API_URL = 'https://api.nasa.gov/neo/rest/v1/feed'
API_URL_TEST = f'{API_URL}?start_date=%s&end_date=%s&api_key=DEMO_KEY'


def main() -> None:
    """
    Main function which parses input and calculates statistics.
    """

    parser = argparse.ArgumentParser(description='Astroid Tracker')
    parser.add_argument('-s', metavar='--s', type=str, help='Start Date for the Asteroid Tracker')
    parser.add_argument('-e', metavar='--e', type=str, help='End Date for the Asteroid Tracker')

    option = parser.parse_args()
    start_date = option.s
    end_date = option.e

    stats = calculate_statistics(start_date, end_date)

    print_statistics(stats)


def calculate_statistics(start_date: str, end_date: str) -> dict:
    """Make an API request and calculate statistics
    :params start_date: Date to search from
    :params end_date:D Date to search to
    :returns: dict
    """

    params = {
        'api_key': 'DEMO_KEY',
        'start_date': start_date,
        'end_date': end_date
    }
    response = requests.get(API_URL, params=params)

    if response.status_code != 200:
        return {'error': json.loads(response.text)}
    api_resp = resp_models.Feed.parse_raw(response.text)

    num_asteroids = api_resp.element_count
    num_potentially_hazardous_asteroids = 0
    largest_diameter_meters: float = 0.0
    nearest_miss_kms: float = 0.0

    for key, near_objects in api_resp.near_earth_objects.items():
        for near_object in near_objects:
            if near_object.is_potentially_hazardous_asteroid:
                num_potentially_hazardous_asteroids += 1

            estimated_diameter_max = near_object.estimated_diameter.meters.estimated_diameter_max
            if largest_diameter_meters < estimated_diameter_max:
                largest_diameter_meters = estimated_diameter_max

            miss_distance = float(near_object.close_approach_data[0].miss_distance.kilometers)
            if not nearest_miss_kms:
                nearest_miss_kms = miss_distance
            else:
                if nearest_miss_kms > miss_distance:
                    nearest_miss_kms = miss_distance

    return {
        'start_date': start_date,
        'end_date': end_date,
        'num_asteroids': num_asteroids,
        'num_potentially_hazardous_asteroids': num_potentially_hazardous_asteroids,
        'largest_diameter_meters': largest_diameter_meters,
        'nearest_miss_kms': nearest_miss_kms,
    }


def print_statistics(stats: dict) -> None:
    """
    Print the calculated statistics.
    """

    logger.info('')

    if 'error' in stats:
        logger.error('HTTP Error:')
        logger.error('Code: %s', stats['error']['code'])
        logger.error('Type: %s', stats['error']['http_error'])
        logger.error('Message: %s', stats['error']['error_message'])

    else:
        logger.info('Displaying asteroid data for period %s - %s' % (stats['start_date'], stats['end_date']))
        logger.info('---------------------------------------------------------------------')
        logger.info('Number of asteroids: %d' % stats['num_asteroids'])
        logger.info('Number of potentially hazardous asteroids: %d' % stats['num_potentially_hazardous_asteroids'])
        logger.info('Largest estimated diameter: %f m' % stats['largest_diameter_meters'])
        logger.info('Nearest miss: %f km' % stats['nearest_miss_kms'])

    logger.info('')


if __name__ == '__main__':
    main()
