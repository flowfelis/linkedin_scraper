import os
from linkedin_scraper import Person, actions
from selenium import webdriver


def main():
    driver = webdriver.Firefox()

    email = "alicand96@gmail.com"
    password = "secret1234"
    actions.login(driver, email, password)  # if email and password isnt given, it'll prompt in terminal
    # person = Person("https://www.linkedin.com/in/andre-iguodala-65b48ab5", driver=driver)
    # person = Person("https://www.linkedin.com/in/ahmet-aydin-41a37a111", driver=driver, get=True,
    #                 close_on_complete=False)

    person = Person("https://www.linkedin.com/in/alican-d%C3%B6nmez-00549098/", driver=driver, get=True,
                    close_on_complete=False)
    print(person)


if __name__ == '__main__':
    main()
