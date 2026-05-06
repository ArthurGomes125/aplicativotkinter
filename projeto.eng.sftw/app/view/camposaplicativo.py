import tkinter as tk
from tkinter import messagebox
from model.ListaUsers import repo, Usuario 

class Campos_Aplicativo(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        tk.Label(self, text="Nome:").grid(row=0, column=0, sticky="w")
        self.entry_nome = tk.Entry(self, width=30)
        self.entry_nome.grid(row=0, column=1, pady=5)

        tk.Label(self, text="Email:").grid(row=1, column=0, sticky="w")
        self.entry_email = tk.Entry(self, width=30)
        self.entry_email.grid(row=1, column=1, pady=5)

        tk.Label(self, text="CPF:").grid(row=2, column=0, sticky="w")
        self.entry_cpf = tk.Entry(self, width=30)
        self.entry_cpf.grid(row=2, column=1, pady=5)

        tk.Label(self, text="Telefone:").grid(row=3, column=0, sticky="w")
        self.entry_telefone = tk.Entry(self, width=30)
        self.entry_telefone.grid(row=3, column=1, pady=5)

        self.btn_submit = tk.Button(self, text="Cadastrar Usuário", command=self.__cadastrar)
        self.btn_submit.grid(row=4, column=0, columnspan=2, pady=10)

        tk.Label(self, text="Usuários Cadastrados:").grid(row=5, column=0, sticky="w", pady=(10, 0))
        self.listbox = tk.Listbox(self, width=50, height=8)
        self.listbox.grid(row=6, column=0, columnspan=2, pady=5)

        self.btn_excluir = tk.Button(self, text="Excluir Selecionado", command=self.exclude_user)
        self.btn_excluir.grid(row=7, column=0, columnspan=2, pady=5)

        self.update_list()

    def __cadastrar(self):
        """Pega os dados da tela e cria um OBJETO da classe Usuario"""
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        cpf = self.entry_cpf.get()
        telefone = self.entry_telefone.get()

        if nome and email:

            novo_usuario = Usuario(nome, email, cpf, telefone)
            
            repo.add_user(novo_usuario)
            
            self.limpar_campos()
            
            self.update_list()
            messagebox.showinfo("Sucesso", f"Usuário {nome} cadastrado com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Por favor, preencha pelo menos Nome e Email.")

    def exclude_user(self):
        """Remove o usuário selecionado na lista"""
        selecionado = self.listbox.curselection()
        if selecionado:
            index = selecionado[0]
            repo.delete_user(index)
            self.update_list()
        else:
            messagebox.showwarning("Aviso", "Selecione alguém na lista para excluir.")

    def update_list(self):
        """Limpa a lista da tela e coloca os nomes dos objetos Usuario"""
        self.listbox.delete(0, tk.END)
        usuarios = repo.get_users()
        
        for user in usuarios:
            texto_para_exibir = user.mostrar_informacoes()
            self.listbox.insert(tk.END, texto_para_exibir)

    def limpar_campos(self):
        """Apaga o texto de todas as caixas de entrada"""
        self.entry_nome.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_cpf.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)