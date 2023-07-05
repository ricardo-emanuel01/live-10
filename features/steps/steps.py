from behave import given, then, when
from selenium import webdriver


dic = {
    'nome': 'name',
    'sobrenome': 'lastName',
    'usuário': 'username',
    'senha': 'passwd',
    'email': 'email',
    'nascimento': 'age',
    'sexo': 'gender',
    'Enviar': 'btnSend'
    }


@given('que o usuario esteja na pagina "{page}"')
def abra_pagina(context, page):
    context.ff = webdriver.Firefox()
    context.ff.get(page)


@when('inserir o {field} "{value}"')
def insere_os_valores_nos_campos(context, field, value):
    context.ff.find_element('id', dic[field]).send_keys(value)


@then('clicar no botao "{butn}"')
def clique_no_botao(context, butn):
    context.ff.find_element('id', dic[butn]).click()


@then('a mensagem devera ser exibida')
def checar_a_mensagem(context):
    mensagem = context.ff.find_element('id', 'text').text
    assert context.text == mensagem
