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


# ---------------------------------------------
# @pytest.fixture(scope='', params='', autouse='', ids='', name='')
# scope: function(default) | class | module | package/session
# params: parametrize -> [] | () | [{},{},...,{}] | ({},{},...,{})
# autouse: auto execution default: False
# ids: variable
# name: alisa
# ---------------------------------------------

@pytest.fixture(
    scope='function',
    autouse=False,
    params=['Java', 'Python', 'Go'], ids=['J', 'P', 'G'],
    name='class_post_processor'
)
def hello_fixture(request):
    print('\nyield::hello_fixture::do pre()')
    yield request.param
    print('\nyield::hello_fixture::do post()')


class TestFixture:
    """
    test fixture
    """

    def test_do_not_fixture(self):
        """
        test_do_not_fixture
        """
        print('\ntest_do_not_fixture')

    def test_do_fixture(self, class_post_processor):
        """
        test_do_fixture
        """
        print('\ntest_do_fixture::' + str(class_post_processor))

    def test_do_auto_fixture(self):
        """
        test_do_auto_fixture
        """
        print('\ntest_do_auto_fixture')

    def test_do_global_fixture(self, global_class_post_processor):
        """
        test_do_auto_fixture
        """
        print('\ntest_do_global_fixture::' + str(global_class_post_processor))
