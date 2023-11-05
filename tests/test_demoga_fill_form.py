from pages.registration_page import RegistrationPage
import allure
from allure_commons.types import Severity


allure.dynamic.title('Проверка формы регистрации: Student Registration Form')
allure.dynamic.tag('Practice Form')
allure.dynamic.label('owner', 'mrantip')
allure.dynamic.severity(severity_level='Critical')
allure.dynamic.feature('Регистрация студента')
allure.dynamic.story('Создаем первую задачу Jenkins')
def test_demoga_fill_form(setup_browser):
    registration_page = RegistrationPage()

    with allure.step('Открываем страницу c формой регистрации'):
        registration_page.open()

    with allure.step('Заполняем First Name'):
        registration_page.fill_first_name('Alesha')
    with allure.step('Заполняем Last Name'):
        registration_page.fill_last_name('Bigd')
    with allure.step('Заполняем Email'):
        registration_page.fill_email('mf666@gmail.com')
    with allure.step('Выбираем Gender'):
        registration_page.choose_gender('Male')
    with allure.step('Заполняем Mobile Number'):
        registration_page.fill_phone_number('0123456789')
    with allure.step('Заполняем Date of Birth'):
        registration_page.choose_birtday(month='2', year='56', day='012')
    with allure.step('Заполняем Subjects'):
        registration_page.choose_subject('Arts')
    with allure.step('Заполняем Hobbies 1'):
        registration_page.choose_hobby_1()
    with allure.step('Заполняем Hobbies 2'):
        registration_page.choose_hobby_2()
    with allure.step('Выбираем Picture'):
        registration_page.uppload_picture('ava.jpg')
    with allure.step('Заполняем Current Address'):
        registration_page.fill_current_address('Heaven')
    with allure.step('Выбираем State'):
        registration_page.choose_state('Uttar Pradesh')
    with allure.step('Выбираем City'):
        registration_page.choose_city('Agra')
    with allure.step('Нажимаем кнопку Submit'):
        registration_page.submit_form()

    with allure.step('Выполняем проверку заполнения полей'):
        registration_page.should_be_registered_form(
            'Alesha Bigd',
            'mf666@gmail.com',
            'Male',
            '0123456789',
            '12 February,1955',
            'Arts',
            'Sports, Reading',
            'ava.jpg',
            'Heaven',
            'Uttar Pradesh Agra'
        )
