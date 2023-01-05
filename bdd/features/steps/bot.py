from behave import given, when, then


@given(u'preenche form Google')
def step_impl(context):
    context.web.get("https://docs.google.com/forms/d/e/1FAIpQLScAckZ7aOpqXwQUtZx6Cfx9Zu6gkEUQfsGAF8PkibyEHOL_yQ/viewform")


@when(u'acesso uma pesquisa')
def step_impl(context):
        context.elementName = context.web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        context.elementName.send_keys('João Mota')
        
        context.elementEmail = context.web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        context.elementEmail.send_keys('motaj@gmail.com')
        
        context.elementAdress = context.web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
        context.elementAdress.send_keys('Rua Olavo Egidio de Souza Aranha, 368 - Ap. 21 - Bloco B')
      
        context.elementPhone = context.web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
        context.elementPhone.send_keys('11 98930 9000')
        
        context.elementComment = context.web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea')
        context.elementComment.send_keys('Teste de automatização da pesquisa do Mota. Por favor!')

@when(u'ao confirmar')
def step_impl(context):
    context.elementSubmit = context.web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    context.elementSubmit.click()

@then(u'a pesquisa é realizada')
def step_impl(context):
    pass