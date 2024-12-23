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


import logging
import os
import time
from datetime import datetime


def makedir_if_necessary(target_path):
    """
    makedir if necessary
    :param target_path:
    """
    if not os.path.exists(target_path):
        os.makedirs(target_path)


class PytestLogger:
    """
    pytest logger
    """

    def __init__(self, project='pytest'):
        """
        设置 logger 日志 path
        """
        root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        logger_path = os.path.join(root_path + os.sep + 'log')

        makedir_if_necessary(logger_path)

        self.log_name = logger_path + os.sep + time.strftime('%Y%m%d%H%M%S') + '.log'
        self.strf_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # 创建一个 名为  ${project} 的 logger
        pylogger = logging.getLogger(project)
        pylogger.setLevel(logging.DEBUG)

        self.logger = pylogger

    def print_console(self, level, message):
        """
        打印日志，支持写入日志和输入到控制台
        """

        # 创建一个 handler，用于写入日志文件
        file_handler = logging.FileHandler(self.log_name, 'a', encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)

        # 再创建一个 handler，用于输出到控制台
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)

        # 定义 handler 的输出格式
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(filename)s[%(lineno)d] - %(levelname)s : %(message)s')

        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        # 给 logger 添加 handler
        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)

        # 记录一条日志
        self.switch(level, message)

        self.logger.removeHandler(stream_handler)
        self.logger.removeHandler(file_handler)

    def debug(self, message):
        """打印debug日志"""
        self.print_console(logging.DEBUG, message)

    def info(self, message):
        """打印普通信息"""
        self.print_console(logging.INFO, message)

    def warning(self, message):
        """打印警告"""
        self.print_console(logging.WARNING, message)

    def error(self, message):
        """打印错误"""
        self.print_console(logging.ERROR, message)

    def switch(self, level, message):
        """
        定义 switch() 来实现 switch 语法
        """
        handler_map = {
            logging.DEBUG: self.logger.debug,
            logging.INFO: self.logger.info,
            logging.WARNING: self.logger.warning,
            logging.ERROR: self.logger.error
        }
        handler = handler_map.get(level)
        if handler:
            handler(message)
