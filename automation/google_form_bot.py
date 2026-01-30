
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def send_form(df):
    browser = webdriver.Edge()
    link = "https://docs.google.com/forms/d/e/1FAIpQLSe2FFVQ4bfdbrHT0zxx6oKAcdwsPPCe4by-_XXE0fESFNOh6Q/viewform"
    browser.get(link)


    for index, row in df.iterrows():  # index = indice identifica cada linha do nosso DF row = linha de cada passo
        NameOrigin = row['nome']
        SurnameOrigin = row['sobrenome']
        EmailOrigin = row['email']
        cpfOrigin = row['cpf']
        CellphoneOrigin = row['celular']
        StateOrigin = row['estado']
        StreetOrigin = row['rua']
        NumberOrigin = row['numero']
        additionalOrigin = row['complemento']

        #preenchimento automático

        sleep(3)

        Name = browser.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(NameOrigin)
        Surname = browser.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(SurnameOrigin)
        Email = browser.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(EmailOrigin)
        Cpf = browser.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(cpfOrigin)
        Cellphone = browser.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(CellphoneOrigin)
        State = browser.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(StateOrigin)
        Street = browser.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys(StreetOrigin)
        Number = browser.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(str(NumberOrigin))
        Additional = browser.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(additionalOrigin)
        Send = browser.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()

        sleep(2)
        browser.get(link)
    browser.quit()