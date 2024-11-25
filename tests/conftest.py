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

import pytest

from localtool.logger.pytest_logger import PytestLogger


@pytest.fixture(
    scope='function',
    autouse=False,
    params=['Java0001', 'Python0010', 'Go0101'],
    ids=['J1', 'P2', 'G3'],
    name='global_class_post_processor'
)
def global_fixture(request):
    """
    global_fixture
    """
    print('\nyield::global_fixture::do pre()')
    yield request.param
    print('\nyield::global_fixture::do post()')


@pytest.fixture(
    scope='session',
    autouse=True
)
def logger():
    handler = PytestLogger()
    return handler
