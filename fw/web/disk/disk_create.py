import time

from selenium.webdriver.common.by import By

from fw.web.any_page import AnyPage

class Locator:
    empty_area = (By.XPATH, '//div[@class="root__content-container"]')
    choose_new_folder = (By.XPATH, '//div[@value="new-folder"]')
    input_name = (By.XPATH, '//div[@class="dialog__body"]//input[contains(@class, "Textinput-Control")]')
    btn_save = (By.XPATH, '//button[contains(@class, "button_submit")]')
    all_files = (By.XPATH, '//div[contains(@class, "listing-item__title")]')


class WebDiskCreate(AnyPage):

    'Создать папку через ПКМ'
    def create_folder_use_right_click(self, folder_name):
        # Нажимаем ПКМ по пустой области
        self.right_click(Locator.empty_area)
        # Выбираем новая папка
        self.click_element(Locator.choose_new_folder)
        # Ждем открытия окна
        time.sleep(0.5)
        # Вводим название папки
        self.send_keys(Locator.input_name, folder_name)
        # Нажимаем на кнопку "Сохранить"
        self.click_element(Locator.btn_save)
        return self

    'Создать файл через ПКМ'
    def create_file_use_right_click(self, file_name, file_type=1):
        '''Типы файлов и их file_type:
            Текстовый документ: 1, Таблица: 2, Презентация, 3, Альбом, 4
        '''
        # Нажимаем ПКМ по пустой области
        self.right_click(Locator.empty_area)
        xpath = (By.XPATH, f'//div[contains(@data-key, "item-{file_type}")]')
        # Нажимаем на выбранный тип файла
        self.click_element(xpath)
        # Ждем открытия окна
        time.sleep(0.5)
        # Вводим название файла
        self.send_keys(Locator.input_name, file_name)
        # Нажимаем на кнопку "Сохранить"
        self.click_element(Locator.btn_save)
        return self

    'Открыть папку по имени'
    def open_folder_by_name(self, folder_name):
        xpath = (By.XPATH, f'//div[@aria-label="{folder_name}"]')
        # Нажимаем на папку двойным нажатием
        self.double_click(xpath)
        return self

    'Получить список всех файлов'
    def get_files_list(self):
        files = []
        # Получаем количество всех файлов
        all_files = len(self.find_elements(Locator.all_files))
        # Проходимся по файлам
        for i in range(1, all_files + 1):
            xpath = (By.XPATH, f'(//div[contains(@class, "listing-item__title")]//span)[{i}]')
            # Получаем имя файла
            file_name = self.get_tag_attribute(xpath, 'title')
            # Записываем имя в список
            files.append(file_name[:-5])
        return files
