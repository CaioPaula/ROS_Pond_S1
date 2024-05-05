# Ponderada ROS-2 Semana 1

## Estrutura de Pastas

```
ROS_Pond_S1
 |- scripts
 |--|- prepare_workspace.sh
 |- src
 |--|- entregador_de_jornal
 |- .gitignore
 |- README.md
```

- `scripts`, pasta que possui os arquivos `.sh`.
- `prepare_workspace.sh`, script que configura todo o workspace ROS, baixando as depencêndias e iniciando o programa da ponderada.
- `src`, pasta que contém o código fonte da ponderada.
- `entregador_de_jornal`, pasta que contém o ROS package.
- `.gitignore`, arquivo que restringe upload de pastas e arquivos desnecessários.
- `README.md`, esse arquivo.


## Como executar o projeto

### Preparando Workspace e Iniciando ponderada

Para executar o programa, criei um arquvo `.sh` que prepara todo o workspace `ROS`, além de executar o código da ponderada.

Os seguinte passos acintecerão.

1. Navegue para a pasta `scripts`.
2. Execute o seguinte commando:
```sh
surce prepare_workspace.sh
```
3. O terminal pedirá a senha de usuário, pois primeiro ele faz a atualização dos pacotes do sistema, para depois crirar o ambiente.
4. Note que um venv foi criado e ativado.
5. Em seguida é clonado o repositório do tutorial de workspace, no diretório `src`.
6. Em seguida, o `colcon` builda o workspace.
7. Logo após, o arquivo local_setup.bash é execeutado.
8. Por fim, o programa da ponderada é executado.

### Rodando turtlesim_node

**OBS:** Note que ao executar o arquivo `scripts/prepare_workspace.sh`, aparecerá no terminal a seguinte menssagem:

```bash
[WARN] [0000000000.000000000] [garbelito_jornaleiro]: Waiting for /spawn service...
```
**Não se preocupe com os números que estão dentro dos colchetes. São o tempo atual do OS.**

Isso significa que o turtlesim turtle_node não está rodando em outro terminal.

Abra um terminal novo e execute:

```bash
ros2 run turtlesim turtlesim_node
```

Pronto Garbelito bananildo está girando :)