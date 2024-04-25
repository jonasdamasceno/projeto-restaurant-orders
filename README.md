# Boas-vindas ao repositório do projeto `Restaurant Orders`!


<details>
  <summary><strong>👨‍💻 O que foi desenvolvido</strong></summary>
    <p>O Restaurante  🍝 🦐 Chapa Quente 🍛 🥘 precisa de você para finalizar sua ferramenta de construção de cardápios. O restaurante necessita desta ferramenta para que possa, de maneira simples, gerar seus cardápios considerando possíveis restrições alimentares e também a disponibilidade dos ingredientes em estoque. Hoje, a gestão das receitas e de estoque do restaurante acontece de forma muito ineficiente através de arquivos csv e, por essa razão, as pessoas fundadoras do estabelecimento desejam melhorar esta gestão.</p>
    <p>Um primeiro time iniciou o desenvolvimento deste projeto e já preparou uma estrutura inicial para que você possa finalizar essa construção. Assim, ao longo deste projeto você será responsável por construir testes para classes já implementadas, implementará uma nova classe para mapear os pratos e suas respectivas receitas (ingredientes e quantidades), também implementará uma classe que gerará os cardápios que devem ser mostrados para as pessoas que frequentam o estabelecimento e outra que fará a gestão de estoque dos ingredientes.</p>
    <p>Lembre-se de construir um <em>código limpo, com boa manutenção e legibilidade</em>. </p>

🚵 Habilidades exercitadas: </br>
  - Praticar o conceito de `Hashmaps` através das estruturas de dados `Dict` e `Set` do Python; </br>
  - Praticar os conhecimentos de testes de software; </br>
  - Praticar os conhecimentos de orientação a objetos. </br>

</details>

<details>

  1. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`

  2. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`
  
  
  
</details>

<details>
  <summary><strong>🧱 Estrutura do Projeto foi desenvolvido pela equipe de curriculo da trybe</strong></summary><br />

  No diretório `src/` você vai encontrar os principais arquivos do projeto, alguns deles já se encontram implementados e outros irão requerer que você os implemente. 

  No diretório `data/` você vai encontrar os arquivos csv que eram utilizados pelas pessoas fundadoras do restaurante para a gestão antiga, eles serão muito importantes para o seu desenvolvimento.

  Este repositório já contém um _template_ com a estrutura de diretórios e arquivos, tanto de código quanto de teste criados. Veja abaixo:

  ```tree
.
├── data
│   ├──🔸 inventory_base_data.csv
│   └──🔸 menu_base_data.csv
├── src
│   ├──🔸 __init__.py
│   ├──🔸 app.py
│   ├── models
│   │   ├──🔸 __init__.py
│   │   ├──🔸 dish.py
│   │   └──🔸 ingredient.py
│   └── services
│       ├──🔸 __init__.py
│       ├──🔹 inventory_control.py
│       ├──🔹 menu_builder.py
│       └──🔹 menu_data.py
├── tests
│   ├──🔸 __init__.py
│   ├──🔸 conftest.py
│   ├── dish
│   │   ├──🔸 __init__.py
│   │   ├──🔸 conftest.py
│   │   ├──🔸 mocks.py
│   │   └──🔹 test_dish.py
│   ├── ingredient
│   │   ├──🔸 __init__.py
│   │   ├──🔸 conftest.py
│   │   ├──🔸 mocks.py
│   │   └──🔹 test_ingredient.py
│   ├──🔸 ingredients.py
│   ├── mocks
│   │   ├──🔸 inventory_base_data.csv
│   │   ├──🔸 inventory_base_data_2.csv
│   │   └──🔸 menu_base_data.csv
│   ├──🔸 test_app.py
│   ├──🔸 test_inventory_control.py
│   ├──🔸 test_menu_builder.py
│   └──🔸 test_menu_data.py
├──🔸 README.md
├──🔸 dev-requirements.txt
├──🔸 pyproject.toml
├──🔸 requirements.txt
├──🔸 setup.cfg
├──🔸 setup.py
├──🔸 trybe-filter-repo.sh
└──🔸 trybe.yml

Legenda:
  🔸 Arquivos que não podem ser alterados.
  🔹 Arquivos a serem alterados para realizar os requisitos.
```

  Na estrutura deste _template_, foi emplementado as classes e métodos necessários.
</details>

<details>
  <summary><strong>🎛 Esse projeto foi desenvolvido utilizando o  Linter</strong></summary><br />

  Para garantir a qualidade do código, vamos utilizar neste projeto o linter `Flake8`.
  Assim o código estará alinhado com as boas práticas de desenvolvimento, sendo mais legível
  e de fácil manutenção! Para rodá-lo localmente no projeto, execute o comandos abaixo:

  ```bash
  python3 -m flake8
  ```

</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual que permite sua máquina rodar, sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  :eyes: Caso precise desativar o ambiente virtual, execute o comando "deactivate". 
  :warning: Lembre-se de ativar novamente o ambiente virtual quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>

<details>
  <summary><strong>🛠 Testes</strong></summary><br />

  Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

  <strong>Executar os testes</strong>

  ```bash
  $ python3 -m pytest
  ```

  O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv
  ```

  Caso precise executar apenas um arquivo de testes basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py
  ```

  Caso precise executar apenas uma função de testes basta executar o comando:

  ```bash
  python3 -m pytest -k nome_da_func_de_tests
  ```

  Se desejar rodar os testes de um arquivo específico, execute com `-x nome_do_arquivo`

  ```bash
  pytest -x tests/test_jobs.py
  ```
  
  Para executar um teste específico de um arquivo, basta executar o comando:

  ```bash
  pytest -x tests/nomedoarquivo.py::test_nome_do_teste
  ```

  Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse [artigo](https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1).
</details>
<details>
  <summary><strong>🗣 Nos dê feedbacks sobre o projeto!</strong></summary><br />
</details>

<details>
  <summary><strong>🗂 Compartilhe seu portfólio!</strong></summary><br />

  Agora que você finalizou os requisitos, chegou a hora de mostrar ao mundo que você aprendeu algo novo! 🚀

  Siga esse [**guia que preparamos com carinho**](https://app.betrybe.com/learn/course/5e938f69-6e32-43b3-9685-c936530fd326/module/a3cac6d2-5060-445d-81f4-ea33451d8ea4/section/d4f5e97a-ca66-4e28-945d-9dd5c4282085/day/eff12025-1627-42c6-953d-238e9222c8ff/lesson/49cb103b-9e08-4ad5-af17-d423a624285a) para disponibilizar o projeto finalizado no seu GitHub pessoal.

</details>

# Requisitos obrigatórios

## 1 - Testando classes já implementadas parte 1

> Implemente testes para a classe `Ingredient`, que se encontra no módulo `src/models/ingredient.py`.

Antes de você começar a trabalhar neste projeto, uma equipe contratada pelo Restaurante  🍝 🦐 Chapa Quente 🍛 🥘  fez a implementação de algumas das classes que serão usadas ao longo do seu desenvolvimento, contudo, a equipe não implementou os testes para estas mesmas classes e cabe a você implementá-los.

A primeira das classes implementadas é a `Ingredient` que representa os ingredientes, um objeto desta classe contém o nome e restrições alimentares do ingrediente como atributos.

A classe já possui alguns métodos mágicos já implementados que garantem funcionalidades específicas. Os métodos já implementados são: `__repr__`, `__eq__` e `__hash__`.

### Implementação

os testes para a classe `Ingredient` foram produzidos no arquivo `tests/ingredient/test_ingredient.py`. Os testes garantiram que:

- a classe pode ser instanciada corretamente de acordo com a assinatura esperada;
- o atributo conjunto `restrictions` é populado como esperado;
- o método mágico `__repr__` funcione como esperado;
- o método mágico `__eq__` funcione como esperado;
- o método mágico `__hash__` funcione como esperado.

</br>

## 2 - Testando classes já implementadas parte 2

> Foram implementados testes para a classe `Dish`, que se encontra no módulo `src/models/dish.py`.

A outra classe testada foi a `Dish`, que representa um prato do cardápio. Uma instância desta classe possui atributos representando o nome, o preço e a receita do prato.

Tal como a classe `Ingredient`, a classe `Dish` já possui alguns métodos já implementados: `add_ingredient_dependency`, `get_restrictions`, `get_ingredients`, `__repr__`, `__eq__` e `__hash__`.

### Implementação

os testes para a classe `Dish` foram implementados no arquivo `tests/dish/test_dish.py`. Os testes garantiram que:

- a classe pode ser instanciada corretamente de acordo com a assinatura esperada;
- os métodos da classe, inclusive os métodos mágicos, funcionem como esperado;
- o dicionário de receita do prato devolve a quantidade correta de um ingrediente;
- são levantados erros ao criar pratos inválidos;

</br>
## 3 - Mapeamento Pratos <> Ingredientes

> Implemente a classe `MenuData` que fará todo o mapeamento de pratos e ingredientes baseado nos arquivo csv disponibilizado. Ela se encontra no módulo `src/services/menu_data.py`.

Hoje, a gestão de pratos e receitas do Restaurante  🍝 🦐 Chapa Quente 🍛 🥘 é feita por meio de um arquivo csv. Em cada linha deste arquivo há o nome do prato, seu preço no cardápio, um dos ingredientes que o compõe e a quantidade necessária daquele ingrediente na receita. Essa organização faz com que um único prato seja representado por múltiplas linhas no mesmo arquivo.

Sua tarefa é implementar uma classe que fará a leitura do arquivo csv mencionado e fará o relacionamento do prato do cardápio com sua respectiva receita, isto é, ingrediente e quantidade. Vale lembrar que já existem classes implementadas para os pratos (`Dish`) e os ingredientes (`Ingredient`). Além disso, a classe que você vai implementar precisa conter um atributo `dishes`, que deverá ser um _set_ que liste todos os pratos presentes no arquivo csv.

### Implementação

a classe `MenuData` foi implementada no arquivo `src/services/menu_data.py`.  
O teste utiliza o [arquivo de mock `tests/mocks/menu_base_data.csv`](./tests/mocks/menu_base_data.csv).

Ao longo da sua implementação você deve garantir que:

- a classe, ao ser instanciada, recebe o caminho para o arquivo csv no parâmetro `source_path`;

- a classe fará a leitura do arquivo csv e baseado em seu conteúdo fará as devidas instanciações de pratos e ingredientes;

- a classe contenha o atributo `dishes` que deverá ser um _set_ com todos os pratos devidamente instanciados;

- cada um dos pratos contenha sua respectiva receita, isto é, seus ingredientes e quantidades, bem como seu preço.

## 4 - Geração dos cardápios

Atualmente o cardápio do Restaurante 🍝 🦐 Chapa Quente 🍛 🥘 tem estrutura fixa e, apesar disso não ser um problema, as pessoas fundadoras do estabelecimento desejavam que este cardápio fosse dinâmico, isso porque muitas das pessoas que frequentam o restaurante possuem restrições alimentares, e seria ideal mostrar-lhes o cardápio contendo apenas os pratos que possam comer.

Com este objetivo, a equipe que trabalhou no projeto antes de você começou a implementação de uma classe que interagisse ao mesmo tempo com o cardápio e com o estoque, e que ainda pudesse exibir os pratos do cardápio de acordo com uma determinada restrição alimentar. Sua tarefa neste requisito é fazer a implementação do método que mostrará os cardápios evitando os pratos com determinada restrição alimentar.

### Implementação

Você deve implementar o método `get_main_menu` dentro da classe `MenuBuilder` que se encontra no arquivo `src/services/menu_builder.py`. O método tem como parâmetro opcional uma restrição que deve ser levada em conta na hora de gerar o cardápio.

Seguindo a assinatura do método que foi deixada pela equipe anterior, o retorno deste método deve ser do tipo `List[Dict]`. Assim, é necessário que o método retorne uma lista de dicionários que contenham as chaves `dish_name`, `ingredients`, `price` e `restrictions` que se referem, respectivamente, ao **nome** do prato, **ingredientes** que o compõem, seu **preço** no cardápio e **restrições** daquele mesmo prato.

Ao longo de sua implementação você deve garantir que:

- a classe possa ser instanciada corretamente;

- o método `get_main_menu` retorna uma lista de dicionários com o cardápio completo quando não é passado nenhum parâmetro;

- o método `get_main_menu` retorna uma lista de dicionários com o cardápio correto respeitando a restrição alimentar passada como parâmetro;

<br>


# Requisitos bônus:

## 5 - Estoque de ingredientes

A gestão de estoque do Restaurante 🍝 🦐 Chapa Quente 🍛 🥘 também é feita por meio de um arquivo csv. Para o controle de estoque é usado um arquivo em que cada uma das linhas contém um ingrediente e sua respectiva quantidade inicial no estoque. Seu objetivo neste requisito é finalizar o desenvolvimento da classe que fará o controle do estoque de ingredientes.

Assim como no requisito anterior, o time que trabalhou antes de você no projeto já iniciou a implementação da classe e cabe a você finalizar esta implementação. Você deve implementar dois métodos para a classe: `check_recipe_availability` e `consume_recipe`.

O primeiro dos métodos (`check_recipe_availability`) deve checar se a receita passada como parâmetro está ou não disponível para consumo, para isso, deve retornar `False` caso um ingrediente da receita não exista no estoque ou caso não exista quantidade suficiente destes ingredientes em estoque e `True`  caso o prato esteja disponível para consumo.

O segundo método (`consume_recipe`) também recebe uma receita como parâmetro, mas deve subtrair a quantidade de ingredientes usados na receita do total disponível em estoque. Vale lembrar que a subtração só deve acontecer caso a receita esteja disponível para consumo, caso contrário, deverá ser levantada uma exceção `ValueError`.

### Implementação

A classe `InventoryMapping` se encontra no arquivo `src/services/inventory_control.py`, nela você deverá implementar os métodos `check_recipe_availability` e `consume_recipe`. Ao longo da sua implementação você deve garantir que:

- A classe possa ser devidamente instanciada;

- o método `check_recipe_availability` retorna `True` caso a receita esteja disponível para consumo e `False` caso contrário;

- o método `consume_recipe` subtrai os ingredientes da receita do total disponível em estoque caso a receita esteja disponível para consumo e levanta uma exceção `ValueError` caso contrário.

## 6 - Cardápios baseados no estoque 

Com a implementação que foi feita até o momento, o método gerador de cardápios, `get_main_menu`, considera apenas as restrições alimentares para fazer a geração do cardápio com os pratos que as pessoas podem comer. Isso ainda é um problema, dado que ainda não é feita a verificação se os ingredientes do prato estão disponíveis em estoque.

Sua tarefa neste requisito é complementar a implementação do método `get_main_menu` para considerar a disponibilidade em estoque dos ingredientes do prato além das restrições alimentares. Assim, o Restaurante 🍝 🦐 Chapa Quente 🍛 🥘 possuirá a ferramenta capaz de gerar cardápios dinâmicos considerando restrições alimentares e disponibilidade em estoque.

<br>

### Implementação

Você deve complementar a implementação do método `get_main_menu`, feito no requisito 4. O método agora precisa considerar também a disponibilidade em estoque dos ingredientes dos pratos. Use a classe implementada no requisito anterior, `InventoryMapping`, para ter acesso a informações do estoque.

Ao longo de sua implementação você deve garantir que:

- o método `get_main_menu` retorna uma lista de dicionários com o cardápio completo caso não exista restrição e todos os ingredientes estiverem disponíveis;

- o método `get_main_menu` retorna uma lista de dicionários com os cardápios corretos respeitando a restrição alimentar passada como parâmetro e também a disponibilidade de ingredientes no estoque;

<br>

<details>
  <summary>
    <b>👀 De olho na dica - Como rodar a aplicação?</b>
  </summary>

Para ver a aplicação rodando com as funcionalidades que você implementou, use o comando a seguir:

```bash
python3 -m uvicorn app:app
```

Acesse a rota `/docs` para ver a [documentação](http://127.0.0.1:8000/docs) gerada pelo FastAPI!

</details>
