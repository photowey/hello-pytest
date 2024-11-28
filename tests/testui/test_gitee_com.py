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

    page.goto("https://gitee.com/")
    page.get_by_role("link", name="登录").click()
    page.wait_for_timeout(1_000)

    page.get_by_placeholder("手机／邮箱／个人空间地址").click()
    page.get_by_placeholder("手机／邮箱／个人空间地址").fill("photowey@gmail.com")
    page.wait_for_timeout(1_000)

    page.get_by_placeholder("请输入密码").click()
    page.get_by_placeholder("请输入密码").fill("flzx_3QC@gitee.com")
    page.wait_for_timeout(1_000)

    page.get_by_role("button", name="登 录").click()

    page.locator(".ml-1").first.click()
    page.wait_for_timeout(1_000)

    page.get_by_text("退出").click()

    # ---------------------
    context.close()
    browser.close()
    playwright.stop()


@allure.feature('测试 Gitee')
@allure.story('测试登录: 成功')
@allure.testcase('https://pytest.happycoding.dev/testcases/gitee/login')
def test_gitee_login():
    with sync_playwright() as playwright:
        run(playwright)
