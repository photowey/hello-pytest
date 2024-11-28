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


class TestLifecycle:
    """
    test lifecycle
    """

    def setup_class(self):
        """
        setup_class
        """
        print('\nexecution setup_class()!')

    def setup(self):
        """
        setup
        """
        print('execution setup()!')

    def teardown(self):
        """
        teardown
        """
        print('execution teardown()!')

    def teardown_class(self):
        """
        teardown_class
        """
        print('execution teardown_class()!')

    def test_lifecycle(self):
        """
        test_lifecycle
        """
        print('execution test_lifecycle()!')
