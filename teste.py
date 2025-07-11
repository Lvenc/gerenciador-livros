from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

console = Console()
livros = []

def menu():
    console.print("\n--- [bold blue]Gerenciador de Livros[/bold blue] ---")
    console.print("1. Adicionar livro")
    console.print("2. Listar livros")
    console.print("3. Editar livro")
    console.print("4. Remover livro")
    console.print("5. Sair")

def adicionar_livro():
    titulo = Prompt.ask("Título do livro")
    autor = Prompt.ask("Autor do livro")
    ano = Prompt.ask("Ano de publicação")
    livro = {"título": titulo, "autor": autor, "ano": ano}
    livros.append(livro)
    console.print(":white_check_mark: [green]Livro adicionado com sucesso![/green]")

def listar_livros():
    if not livros:
        console.print(":open_mailbox_with_mail: [yellow]Nenhum livro cadastrado.[/yellow]")
        return
    table = Table(title="📚 Lista de Livros")
    table.add_column("Nº", justify="right", style="cyan")
    table.add_column("Título", style="magenta")
    table.add_column("Autor", style="green")
    table.add_column("Ano", justify="center", style="yellow")
    for i, livro in enumerate(livros, 1):
        table.add_row(str(i), livro['título'], livro['autor'], livro['ano'])
    console.print(table)

def editar_livro():
    listar_livros()
    try:
        index = int(Prompt.ask("Digite o número do livro para editar")) - 1
        if 0 <= index < len(livros):
            console.print("Deixe em branco para manter o valor atual.")
            novo_titulo = Prompt.ask("Novo título", default=livros[index]['título'])
            novo_autor = Prompt.ask("Novo autor", default=livros[index]['autor'])
            novo_ano = Prompt.ask("Novo ano", default=livros[index]['ano'])
            livros[index] = {"título": novo_titulo, "autor": novo_autor, "ano": novo_ano}
            console.print(":white_check_mark: [green]Livro atualizado com sucesso![/green]")
        else:
            console.print(":cross_mark: [red]Número inválido.[/red]")
    except ValueError:
        console.print(":cross_mark: [red]Entrada inválida.[/red]")

def remover_livro():
    listar_livros()
    try:
        index = int(Prompt.ask("Digite o número do livro para remover")) - 1
        if 0 <= index < len(livros):
            removido = livros.pop(index)
            console.print(f":wastebasket: [red]Livro '{removido['título']}' removido com sucesso![/red]")
        else:
            console.print(":cross_mark: [red]Número inválido.[/red]")
    except ValueError:
        console.print(":cross_mark: [red]Entrada inválida.[/red]")

while True:
    menu()
    opcao = Prompt.ask("Escolha uma opção")
    if opcao == "1":
        adicionar_livro()
    elif opcao == "2":
        listar_livros()
    elif opcao == "3":
        editar_livro()
    elif opcao == "4":
        remover_livro()
    elif opcao == "5":
        console.print("📕 Encerrando o sistema...")
        break
    else:
        console.print(":cross_mark: [red]Opção inválida.[/red]")
