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

import pymysql

from localtool.mysql.option import Options


class Mysql(object):

    def __init__(self, options: Options):
        self.options = options
        connection = self.connection()
        self.connection = connection

    def connection(self) -> pymysql.connect:
        connection: pymysql.connect = pymysql.connect(
            host=self.options.host, user=self.options.user,
            password=self.options.password, database=self.options.database, port=self.options.port)

        return connection

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()

    def insert(self, sql: str, parameters: []):
        rows = 0
        cursor = self.connection.cursor()
        for parameter in parameters:
            single_rows = cursor.execute(sql, parameter)
            rows += single_rows
        cursor.close()
        self.commit()
        self.close()

        return rows
