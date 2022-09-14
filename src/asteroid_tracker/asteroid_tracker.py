"""
The Asteroid Tracker program
"""
from __future__ import annotations

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


def calculate_statistics(start_date: str, end_date: str) -> resp_models.Stats | resp_models.Error:
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
        error = json.loads(response.text)
        return resp_models.Error(
                error=resp_models.Details(
                        code=error['code'],
                        request=error['request'],
                        http_error=error['http_error'],
                        error_message=error['error_message']
                )
        )

    neo_feed = resp_models.Feed.parse_raw(response.text)
    neo_feed.calc_feed_stats()

    return resp_models.Stats(
            start_date=start_date,
            end_date=end_date,
            num_asteroids=neo_feed.num_asteroids,
            num_potentially_hazardous_asteroids=neo_feed.num_potentially_hazardous_asteroids,
            nearest_miss_kms=neo_feed.nearest_miss_kms,
            largest_diameter_meters=neo_feed.largest_diameter_meters
    )


def print_statistics(stats: resp_models.Stats | resp_models.Error) -> None:
    """
    Print the calculated statistics.
    """

    logger.info('')

    if isinstance(stats, resp_models.Error):
        logger.error('HTTP Error:')
        logger.error('Code: %s', stats.error.code)
        logger.error('Type: %s', stats.error.http_error)
        logger.error('Message: %s', stats.error.error_message)

    else:
        logger.info('Displaying asteroid data for period %s - %s' % (stats.start_date, stats.end_date))
        logger.info('---------------------------------------------------------------------')
        logger.info('Number of asteroids: %d' % stats.num_asteroids)
        logger.info('Number of potentially hazardous asteroids: %d' % stats.num_potentially_hazardous_asteroids)
        logger.info('Largest estimated diameter: %f m' % stats.largest_diameter_meters)
        logger.info('Nearest miss: %f km' % stats.nearest_miss_kms)

    logger.info('')


if __name__ == '__main__':
    main()
