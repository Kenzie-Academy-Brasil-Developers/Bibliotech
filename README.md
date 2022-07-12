# Bibliotech
Gerenciamento de biblioteca

# Campos a serem adicionados no DER:

user: password, created_at, is_admin, is_debt (boolean)

loan: is_returned (default False)

# Regras de negocio

Um usuario pode emprestar apenas três livros por vez.

Tempo de devolução 30 dias.

Caso nao retorne is_debt é setado para **TRUE**.

Usuario com is_debt true, não é permitido pegar novos livros.

Quando devolvido o livro, setar a coluna is_returned da tabela loan para **TRUE**

Usuario é permitido pegar outro livro, quando não ouver pendencias.

# Rotas

# User

**POST** /api/user/signup - Criação de usuario

```
Body
{
	email
	username
	full_name
	password,
	birth_date,
	phone,
}
```

**POST** /api/user/signin - Autenticação
```
Body
{
	email
	password
}
```

GET /api/user - Listagem de usuarios (ADMIN)
Sem Body

PATCH /api/user/:user_id - Alteracao de dados (Autenticado, proprio usario ou ADMIN)
```
{
  Body
	full_name
	email,
	birth_date,
	password,
}
```

DELETE /api/user/:user_id - deletar usuario (Autenticado, proprio usuario ou ADMIN)


# livros
GET /api/book (Sem autenticação) - Listagem
Possiveis filtros:
- Title (Inteiro ou partes)
- Genre
- author_name (Inteiro ou partes)
(Exemplo: api/book?title=banana)

**GET** /api/book/:book_id (Sem autenticação) - Pegar livro por id


**POST** /api/book (Com autenticação) - criação de livros
```
{
	title,
	pages,
	author_id (nome por enquanto),
	classification,
	capa_url,
}
```

**PUT** /api/book/:book_id (Com autenticação) - Alterar dados do livro 
```
{ 
	title
	pages,
	classification,
	capa_url,
}
```

**DELETE** /api/book/:book_id (Com autenticação ADMIN)- Deletar livro

**POST** /api/book/loan - Emprestimo de livros

Maximo de três.
```
Body
{
  [book_id]
}
```

# Reviews

GET /api/book/:id/review - Listagem de reviews a partir do id do livro.

POST /api/book/:id/review - Criação de review
```
body
  text (string),
  recomendation (string),
  stars (integer),
  review_type (string)
```


PATCH /api/book/:id/review/:id - Alteraçao de review
```
body
{
  text (string),
  recomendation (string),
  stars (integer),
  review_type (string)
}
```

DELETE /api/book/:id/review/:id - Deleção de view
