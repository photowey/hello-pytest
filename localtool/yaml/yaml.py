# -*- coding:utf-8 -*-


#  Copyright © 2024 the original author or authors.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


import yaml


class YmlReader:
    """
    yml reader
    """

    def __init__(self, yml_file):
        """
        init yml file
        """
        self.yml_file = yml_file

    def read_yml(self):
        """
        read yml file
        """
        try:
            with open(self.yml_file, 'r', encoding='utf-8') as f:
                content = yaml.load(f, Loader=yaml.FullLoader)
                return content
        except FileNotFoundError as e:
            print('file not found!!! {}'.format(e))
        except TypeError as t:
            print('the type of file is wrong!!! {}'.format(t))
