# Bibliotech
- [Objetivo](#objetivo)
- [EndPoints](#endpoints)
	1. [Usuário](#user)
	1. [Livros](#livros)
	1. [Reviews](#reviews)
- [Regras de negócio](#regras-de-negocio)



## Objetivo
Muitas vezes ao pensar em biblioteca imaginamos coisas 
enormes, como vemos nos filmes mas não podemos 
esquecer que existem também muitas outra bibliotecas 
menores que são importantíssimas, nas escolas, nas 
igrejas, em algumas cidades as bibliotecas comunitárias, 
nas faculdades e também colecionadores possuem suas 
bibliotecas particulares. E manter a organização disso 
requer muito cuidado. Pensando nisso a Bibliotech 
centraliza todas as informações necessárias para fazer 
esse gerenciamento de forma simples.
A ideia é criar um gerenciador para biblioteca, que 
contenha informações de usuários, livros e reviews 
disponibilizando um ambiente que as informações sejam 
de fácil acesso tanto para os administradores da 
biblioteca quanto para os usuários


---

## EndPoints

### Usuários

<table>
	<thead>
		<tr>
			<th>Método</th>
			<th>Rota</th>
			<th>Descrição</th>
			<th>Permissão</th>
			<th>Details</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="color: lime;">POST</td>
			<td>/api/user/signup</td>
			<td>Criação de um usuário</td>
			<td>NONE</td>
			<td>
				<details>
					<summary>Body</summary>
					<ul>
						<li>email</li>
						<li>password</li>
						<li>fullName</li>
						<li>birthDate</li>
					</ul>
				</details>
			</td>
		</tr>
		<tr>
			<td style="color: lime;">POST</td>
			<td>/api/user/signin</td>
			<td>Gerar token para autenticação</td>
			<td>NONE</td>
			<td>
				<details>
					<summary>Body</summary>
					<ul>
						<li>email</li>
						<li>password</li>
					</ul>
				</details>
			</td>
		</tr>
		<tr>
			<td style="color: #9d00ff;">GET</td>
			<td>/api/user</td>
			<td>Listagem de todos os usuários</td>
			<td>ADMIN</td>
			<td>NONE</td>
		</tr>
		<tr>
			<td style="color: #9d00ff;">GET</td>
			<td>/api/user/:user_id</td>
			<td>Listagem de um usuário</td>
			<td>OWNER ou ADMIN</td>
			<td>NONE</td>
		</tr>
		<tr>
			<td style="color: orange;">PATCH</td>
			<td>/api/user/:user_id</td>
			<td>Alterar dados de um usuário</td>
			<td>OWNER ou ADMIN</td>
			<td>
				<details>
					<summary>Body</summary>
					<ul>
						<li>email</li>
						<li>fullName</li>
						<li>birthDate</li>
						<li>password</li>
					</ul>
				</details>
			</td>
		</tr>
		<tr>
			<td style="color: red;">DELETE</td>
			<td>/api/user/:user_id</td>
			<td>Exclusão de um usuário</td>
			<td>OWNER ou ADMIN</td>
			<td>NONE</td>
		</tr>
	</tbody>
</table>

---

## Livros
<table>
	<thead>
		<tr>
			<th>Método</th>
			<th>Rota</th>
			<th>Descrição</th>
			<th>Permissão</th>
			<th>Details</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="color: #9d00ff;">GET</td>
			<td>/api/book</td>
			<td>Listagem de todos os livros</td>
			<td>NONE</td>
			<td>NONE</td>
		</tr>
		<tr>
			<td style="color: #9d00ff;">GET</td>
			<td>/api/book/:book_id</td>
			<td>Listagem de um livro pelo id</td>
			<td>NONE</td>
			<td>NONE</td>
		</tr>
		<tr>
			<td style="color: lime;">POST</td>
			<td>/api/book</td>
			<td>Cadastro de um livro</td>
			<td>ADMIN</td>
			<td>
				<details>
					<summary>Body</summary>
					<ul>
						<li>title</li>
						<li>authorId</li>
						<li>classification</li>
						<li>bookImgUrl</li>
					</ul>
				</details>
			</td>
		</tr>
		<tr>
			<td style="color: orange;">PATCH</td>
			<td>/api/book/:book_id</td>
			<td>Atualização dos dados de um livro</td>
			<td>ADMIN</td>
			<td>NONE</td>
		</tr>
		<tr>
			<td style="color: red;">DELETE</td>
			<td>/api/book/:book_id</td>
			<td>Exclusão de um livro pelo id</td>
			<td>ADMIN</td>
			<td>NONE</td>
		</tr>
	</tbody>
</table>

---
## Empréstimo

<table>
	<thead>
		<tr>
			<th>Método</th>
			<th>Rota</th>
			<th>Descrição</th>
			<th>Permissão</th>
			<th>Details</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="color: #9d00ff;">GET</td>
			<td>/api/loan</td>
			<td>Listagem de todos os emprestimos do usuario fazendo a requisição</td>
			<td>USER</td>
			<td>
				NONE
			</td>
		</tr>
		<tr>
			<td style="color: #9d00ff;">GET</td>
			<td>/api/loan/all</td>
			<td>Listagem de TODOS os emprestimos</td>
			<td>USER</td>
			<td>
				NONE
			</td>
		</tr>
		<tr>
			<td style="color: #9d00ff;">GET</td>
			<td>/api/user/:user_id/loan</td>
			<td>Listagem de todos os emprestimos de um usuário</td>
			<td>ADMIN</td>
			<td>NONE</td>
		</tr>
		<tr>
			<td style="color: lime;">POST</td>
			<td>/api/loan</td>
			<td>Fazer emprestimo de 1 até 3 livros</td>
			<td>USER</td>
			<td>
				<details>
					<summary>Body</summary>
					Lista de ids, máximo 3
					<ul>
						<li>[book_id]</li>
					</ul>
				</details>
			</td>
		</tr>
		<tr>
			<td style="color: orange;">PATCH</td>
			<td>/api/loan:loan_id</td>
			<td>Remove um emprestimo</td>
			<td>ADMIN</td>
			<td>
				<details>
					<summary>Body</summary>
					<ul>
						<li>isReturned</li>
					</ul>
				</details>
			</td>
		</tr>
	</tbody>
</table>

---

## Reviews

<table>
<thead>
		<tr>
			<th>Método</th>
			<th>Rota</th>
			<th>Descrição</th>
			<th>Permissão</th>
			<th>Details</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="color: #9d00ff;">GET</td>
			<td>/api/book/:id/review</td>
			<td>Listagem de reviews a partir do id do livro.</td>
			<td>NONE</td>
			<td>NONE</td>
		</tr>
		<tr>
			<td style="color: lime;">POST</td>
			<td>/api/book/:id/review</td>
			<td>Criação de reviews</td>
			<td>USER</td>
			<td>
				<details>
					<summary>Body</summary>
					<ul>
						<li>text</li>
						<li>recomendation</li>
						<li>stars</li>
						<li>reviewType</li>
					</ul>
				</details>
			</td>
		</tr>
		<tr>
			<td style="color: orange;">PATCH</td>
			<td>/api/book/:id/review/:id</td>
			<td>Alteração de uma review</td>
			<td>OWNER or ADMIN</td>
			<td>
				<details>
					<summary>Body</summary>
					<ul>
						<li>text</li>
						<li>recomendation</li>
						<li>stars</li>
						<li>reviewType</li>
					</ul>
				</details>
			</td>
		</tr>
		<tr>
			<td style="color: red;">DELETE</td>
			<td>/api/book/:id/review/:id</td>
			<td>Deleção de review</td>
			<td>OWNER or ADMIN</td>
			<td>NONE</td>
		</tr>
	</tbody>
</table>


# Regras de negocio

Um usuario pode emprestar apenas três livros por vez.

Tempo de devolução 30 dias.

Caso nao retorne is_debt é setado para **TRUE**.

Usuario com is_debt true, não é permitido pegar novos livros.

Quando devolvido o livro, setar a coluna is_returned da tabela loan para **TRUE**

Usuario é permitido pegar outro livro, quando não ouver pendencias.