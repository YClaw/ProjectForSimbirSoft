from fw.web.any_page import AnyPage

from selenium.webdriver.common.by import By

class Locator:
    password = (By.ID, 'passp-field-passwd')
    login = (By.ID, 'passp-field-login')
    btn_sign_in = (By.ID, 'passp:sign-in')
    btn_exit = (By.XPATH, '//a[contains(@class,"action_exit")]')
    user_account = (By.XPATH, '//a[contains(@class,"current-account")]')

class Login(AnyPage):

    'Вход по логину и паролю'
    def login_by_log_pass(self, login=None, password=None):
        if login is None and password is None:
            login = self.manager.group_data.users['TestLapaev']['login']
            password = self.manager.group_data.users['TestLapaev']['password']
        # Вводим логин
        self.send_keys(Locator.login, login)
        # Нажимаем на кнопку "Войти"
        self.click_element(Locator.btn_sign_in)
        # Вводим пароль
        self.send_keys(Locator.password, password)
        # Нажимаем на кнопку "Войти"
        self.click_element(Locator.btn_sign_in)
        return self

    'Разлогиниться'
    def log_out(self):
        # Нажимаем на иконку аватара
        self.click_element(Locator.user_account)
        # В списке нажимаем на "Выйти"
        self.click_element(Locator.btn_exit)
        return self