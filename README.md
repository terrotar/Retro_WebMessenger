# Code_Challenge_Yungas

********** Introdução **********

Olá, seja bem-vindo ao WebMessenger, um projeto de webchat ao vivo como nos tempos antigos e remotos de sites de bate-papo kkkkkk
Brincadeiras a parte, obrigado pela oportunidade de desenvolver esse projeto. Eu não tenho tanta experiência na área de TI, nunca tinha tido contato com websockets, para ser sincero nem conhecia os seus conceitos, e muito menos o svelte, o qual nunca tinha ouvido falar. Foi um desafio gigante para mim, pŕincipalmente pela dificuldade que tive de compreender primeiro os conceitos de websocket para então poder aplicar no projeto. Além disso, me deparei o com JQuery, o qual também nunca havia trabalhado, porém consegui algumas conquistas com ele. Eu foquei meu projeto no back-end, fiz um pequeno planejamento dos caminhos que deveria tomar para conseguir realizar a entrega do projeto como gostaria mas infelizmente não consegui concluir ele a tempo do prazo de entrega e por este motivo irei continuar com ele até conseguir completá-lo para me aprimorar profissionalmente e também gostaria de conseguir realizar um front-end legal para a aplicação com o svelte futuramente.

Achei muito legal as recomendações do que usar para desenvolver o projeto, vi o FastAPI(realizei um projeto com ele) e o próprio svelte(o qual nunca utilizei), uma coisa que não é muito comum as empresas incentivarem essas ferramentas mais novas e isso destacou muito a forma como a empresa se porta frente às novidades. O próprio tema do desafio foi bem legal, apesar de eu ter literalmente perdido o sono com a implementação do socketio kkkk foi muito proveitoso para mim e um desafio muito grande.

Houve algumas partes do desafio na parte avançada(realizar um register/login com senha hask, etc) o qual estava muito mais familiarizado e achei relativamente fácil, diferente de diversas coisas do básico(implementação do websocket) e algumas funções(typing, stop typing). O Jquery foi um desafio a mais no meio disso tudo, enquanto estava tentando entender como funciona e realizar um 'connect' com algum cliente na room tinha que realizar uma função com o Jquery no '.html' e isso me atrasou ainda mais nos meus planos, mas o conhecimento que absorvi foi gigante e o horizonte expandiu de forma absurda.

Agradeço novamente a oportunidade e espero que curta a prévia do que será um dia esse projeto, o WebMessenger, um bate-papo das antigas estilo retro !!!

********** Requerimentos **********

Os pacotes para serem intalados se encontram no arquivo 'Pipfile', tendo todos os nomes e versões dos mesmos. Para rodar corretamente a aplicação, instale-os previamente.

********** Como rodar a aplicação **********

Para iniciar o programa é necessário estar na pasta raiz do projeto e rodar o arquivo 'main.py'.
IMPORTANTE: Não utilize o commando 'flask run', pois para tirar o maior proveito do socketio é necessário roda-lo pelo proprio socketio.

********** Observações **********

Há alguns bugs na aplicação como esperado visto as dificuldades já comentadas com a aplicação. Uma delas é que caso você esteja logado e esteja na route da room01 e abrir outra página com a mesma route, o server emite uma mensagem de boas vindas mesmo que o usuário já esteja na sala.

Outro bug que encontrei foi na mesma situação anterior, um usuário logado e com duas abas abertas na route da room01, caso em uma das páginas do cliente deslogue, a outra página que estava na room01 não é deslogada automaticamente e ainda é possível enviar e receber mensagens pelo socketio.
