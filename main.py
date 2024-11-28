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


import os

import pytest


def clean_tmp_dir(target_path):
    """
    clean tmp dir
    """

    if os.path.exists(target_path):
        sub_files = os.listdir(target_path)
        for i in sub_files:
            sub_file = os.path.join(target_path, i)
            if os.path.isdir(sub_file):
                clean_tmp_dir(sub_file)
            else:
                print('remove the file:{}'.format(sub_file))
                os.remove(sub_file)


if __name__ == '__main__':
    # ---------------------------------------------
    # -s: 输出调试信息，包括打印信息
    # pytest.main(['-s'])
    # -v: 详细信息
    # pytest.main(['-v'])

    # ---------------------------------------------
    # 所有
    # pytest.main(['-vs'])
    # ---------------------------------------------

    # ---------------------------------------------
    # 指定用例
    # pytest.main(['-vs', './tests/testapi/test_api.py'])
    # ---------------------------------------------

    # ---------------------------------------------
    # 指定文件夹
    # pytest.main(['-vs', './tests/testapi'])
    # ---------------------------------------------

    # ---------------------------------------------
    # 通过 nodeId 指定运行的用例
    # nodeId: 模块名-分隔符-类名-方法名-函数名 组成
    # ---------------------------------------------

    # ---------------------------------------------
    # 执行函数
    # pytest.main(['-vs', './tests/testapi/test_api.py::test_function'])
    # ---------------------------------------------

    # ---------------------------------------------
    # 执行方法
    # pytest.main(['-vs', './tests/testapi/test_api.py::TestInterface::test_method'])
    # ---------------------------------------------
    # -n: 线程数量
    # --reruns: 失败用例重试 (--reruns==2)
    # -x: 只要有一个用例报错,就停止
    # -k: 根据用例的部分名称--模糊匹配 $ pytest -vs [path] -k "hello"
    # @pytest.mark.run(order=2) 改变执行顺序
    # ---------------------------------------------

    # ---------------------------------------------
    # 采用 pytest.ini
    # 自定义-分组
    # $ pytest -m "smoke or stage"
    # ---------------------------------------------

    # warning::it's dangerous
    clean_tmp_dir('./tmp')

    pytest.main()
    os.system('allure generate ./tmp -o ./report --clean')
