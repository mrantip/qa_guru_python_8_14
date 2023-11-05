import resource

from selene import browser, have, be


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').click().type(value)

    def choose_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()

    def fill_phone_number(self, value):
        browser.element('#userNumber').type(value)

    def choose_birtday(self, month, year, day):
        browser.element('#dateOfBirthInput').should(be.visible).click()
        browser.element(f'.react-datepicker__month-select > option:nth-child({month})').click()
        browser.element(f'.react-datepicker__year-select > option:nth-child({year})').click()
        browser.element(f'.react-datepicker__day.react-datepicker__day--{day}').click()

    def choose_subject(self, value):
        browser.element("#subjectsInput").type(value).press_enter()

    def choose_hobby_1(self):
        browser.element('[for="hobbies-checkbox-1"]').click()

    def choose_hobby_2(self):
        browser.element('[for="hobbies-checkbox-2"]').click()

    def choose_hobby_3(self):
        browser.element('[for="hobbies-checkbox-3"]').click()

    def uppload_picture(self, value):
        browser.element('#uploadPicture').type(resource.path(value))

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)

    def choose_state(self, value):
        browser.element('#react-select-3-input').type(value).press_enter()

    def choose_city(self, value):
        browser.element('#react-select-4-input').type(value).press_enter()

    def submit_form(self):
        browser.element('#submit').execute_script('element.click()')

    def should_be_registered_form(self, full_name, email, gender, phone_number, date_of_birth, subject, hobby, picture,
                                  state, city):
        browser.element('.modal-content').should(be.visible)
        browser.all(".table-dark>tbody>tr>td:nth-child(2)").should(have.texts(
            full_name,
            email,
            gender,
            phone_number,
            date_of_birth,
            subject,
            hobby,
            picture,
            state,
            city
        ))
