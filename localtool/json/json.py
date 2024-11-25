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

import json


class JSON(object):
    """
    utilities function of JSON.
    """

    @staticmethod
    def transfer_object(body: object) -> str:
        """
        Serialize the object to a JSON string.\n
        :param body:
        :return:
        """
        return json.dumps(body)

    @staticmethod
    def to_json_string(dict_body: dict) -> str:
        """
        Serialize the dict object to a JSON string.\n
        :param dict_body:
        :return:
        """
        return json.dumps(dict_body)

    @staticmethod
    def to_json_strings(dict_body: list) -> str:
        """
        Serialize the list object to a JSON string.\n
        :param dict_body:
        :return:
        """
        return json.dumps(dict_body)

    @staticmethod
    def to_pretty_json_string(dict_body: dict) -> str:
        """
          Serialize the dict object to a pretty JSON string.\n
          :param dict_body:
          :return:
          """
        return json.dumps(dict_body, sort_keys=True, indent=4)

    @staticmethod
    def to_pretty_json_strings(dict_body: list) -> str:
        """
        Serialize the list object to a pretty JSON string.\n
        :param dict_body:
        :return:
        """
        return json.dumps(dict_body, sort_keys=True, indent=4)

    @staticmethod
    def parse_object(json_str: str) -> dict:
        """
        Deserialize the JSON string into a dict-object.\n
        :param json_str:
        :return:
        """
        return json.loads(json_str)

    @staticmethod
    def parse_array(json_str: str) -> list:
        """
        Deserialize the JSON string into a list-object.\n
        :param json_str:
        :return:
        """
        return json.loads(json_str)
