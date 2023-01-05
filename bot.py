from selenium import webdriver
import time

class bot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def preencherForms(self):
        drive = self.driver
        drive.get('https://docs.google.com/forms/d/e/1FAIpQLScAckZ7aOpqXwQUtZx6Cfx9Zu6gkEUQfsGAF8PkibyEHOL_yQ/viewform')

        elementName = drive.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        elementName.send_keys('Alex Ferreira')
        time.sleep(6)
        
        elementEmail = drive.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        elementEmail.send_keys('ferreirinha@gmail.com')
        time.sleep(6)
        
        elementAdress = drive.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
        elementAdress.send_keys('Rua Olavo Egidio de Souza Aranha, 368 - Ap. 21 - Bloco B')
        time.sleep(6)
      
        elementPhone = drive.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
        elementPhone.send_keys('11 98730000')
        time.sleep(6)
        
        elementComment = drive.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea')
        elementComment.send_keys('Teste de automatização da pesquisa do DEDE. Por favor!')
        time.sleep(6)
        
        elementSubmit = drive.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        elementSubmit.click()
        time.sleep(10)
                       
bot = bot()
bot.preencherForms()