#     Copyright 2019 Jonathan Niven
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#
import argparse
from pathlib import Path
from typing import Dict, List


class WorkLog:
    """TODO"""
    def __init__(self):
        """TODO"""
        # TODO: Create work log object based on what toggl provides


class TogglServer:
    """TODO"""
    def __init__(self):
        """TODO"""
        # TODO: Initialise with all needed configuration points

    def get_work(self, time_period) -> List[WorkLog]:
        """TODO"""
        # TODO: Return all logged work instances within a given time period


class JiraServer:
    """TODO"""
    def __init__(self):
        """TODO"""
        # TODO: Initialise with all needed configuration points

    def log_work(self, ticket_number: str, work_log: WorkLog):
        """TODO"""
        # TODO: Push work log object to the provided ticket number


def parse_args() -> argparse.Namespace:
    """"""
    parser = argparse.ArgumentParser(
        description='Logs time on jira tickets from toggl records based on '
                    'tags')
    parser.add_argument('--config', '-c', dest='config', default='config.yml',
                        help='Yaml file for configuring both servers')
    args = parser.parse_args()
    return args


def get_secret_data(secrets_file: Path) -> Dict:
    """Reads the secrets file used to store API keys

    :param secrets_file: The yml file containing the secrets
    :return: The secret mappings
    """



def main():
    """"""


if __name__ == '__main__':
    main()
