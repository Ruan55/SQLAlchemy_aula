# SQLAlchemy_aula

## Aula 1
- ORM e Conceitos Iniciais
- SQLAlchemy é o kit de ferramentas Python SQL e Object Relational Mapper que dá aos desenvolvedores de aplicativos todo o poder e flexibilidade do SQL.
- Mapeamento objeto-relacional (ou ORM, do inglês: Object-relational mapping) é uma técnica de desenvolvimento utilizada para reduzir a impedância da programação orientada aos objetos utilizando bancos de dados relacionais. As tabelas do banco de dados são representadas através de classes e os registros de cada tabela são representados como instâncias das classes correspondentes.

## Aula 2
- O Engine é o ponto de partida para qualquer aplicação SQLAlchemy. Itilit “home base” para a base de dados real e a sua DBAPI, entregue ao SQLAlchemy aplicação através de um pool de conexão e um Dialect, que descreve como para falar com um tipo específico de combinação de banco de dados/DBAPI.
- Ex: db = create_engine("sqlite:///meubanco.db")

- Um pool de conexão é uma técnica padrão usada para manter conexões de longa duração na memória para reutilização eficiente bem como para fornecer gerenciamento para o número total de conexões de um aplicativo pode usar simultaneamente.
Particularmente para aplicativos web do lado do servidor, um pool de conexão é a maneira padrão de manter um “pool” de ligações de base de dados ativas na memória que são reutilizado em todas as solicitações.
SQLAlchemy inclui várias implementações de pool de conexão que se integram com o Engine. Eles também podem ser usados diretamente para aplicativos que desejam adicionar pooling a um abordagem DBAPI simples.
- Ex: db = create_engine("postgresql://me@localhost/mydb", pool_size=20, max_overflow=0)
