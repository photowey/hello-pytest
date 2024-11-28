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


import pandas as pd


class ExcelReader(object):
    """
    read excel
    """

    def __init__(self, excel_file: str):
        self.excel_file = excel_file

    def read_excel(self, sheet_name='sheet1', index_col=1, fillna=True, engine='openpyxl') -> list:
        """
        read excel by pandas lib, use openpyxl engine.
        """
        try:
            with open(self.excel_file, 'rb') as file_bin:
                data = pd.read_excel(file_bin, sheet_name=sheet_name, index_col=index_col, engine=engine)
                if fillna:
                    data.fillna('', inplace=True)
                value_list = data.values.tolist()
                return value_list
        except FileNotFoundError as e:
            print('file not found! {}'.format(e))
        except TypeError as t:
            print('file type error! {}'.format(t))
