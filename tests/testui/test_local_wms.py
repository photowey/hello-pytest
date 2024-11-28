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


import allure
from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://wms.happycoding.dev")
    page.wait_for_timeout(1_000)

    with page.expect_popup() as login_page:
        page.get_by_text("前往入库").click()

    page.wait_for_timeout(1_000)

    login = login_page.value
    login.get_by_placeholder("账号").click()
    login.get_by_placeholder("账号").fill("admin")
    page.wait_for_timeout(1_000)

    login.get_by_placeholder("密码").click()
    login.get_by_placeholder("密码").fill("admin123")
    page.wait_for_timeout(1_000)

    login.get_by_role("button", name="登 录").click()

    # ---------------------
    context.close()
    browser.close()
    playwright.stop()


@allure.feature('测试 WMS')
@allure.story('测试登录: 成功')
@allure.testcase('https://pytest.happycoding.dev/testcases/happycoding/login')
def test_local_wms():
    with sync_playwright() as playwright:
        run(playwright)
