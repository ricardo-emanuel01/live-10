# language:pt



Funcionalidade: Cadastro
  Cenário: Efetuar o cadastro com sucesso
    Dado que o usuario esteja na pagina "http://localhost:8080/cadastro"
    Quando inserir o nome "Ricardo"
    E inserir o sobrenome "Oliveira"
    E inserir o usuário "riczd"
    E inserir o sexo "Masculino"
    E inserir o senha "123456"
    E inserir o email "ricardo@gmail.com"
    E inserir o nascimento "02/03/2002"
    Então clicar no botao "Enviar"
    E a mensagem devera ser exibida
      """
      Bem vindo Ricardo
      Usuário: riczd
      Senha: 123456
      """
    