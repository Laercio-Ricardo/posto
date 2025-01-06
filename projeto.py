import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

# Função para carregar a planilha e gerar os dados
def carregar_planilha():
    try:
        # Carregar a planilha Excel
        arquivo_excel = 'arquivo.xlsx'  # Substitua pelo caminho do seu arquivo Excel
        df = pd.read_excel(arquivo_excel, engine='openpyxl')

        # Verificar se a planilha tem a estrutura correta
        if df.empty:
            messagebox.showerror("Erro", "A planilha está vazia.")
            return None, [], []

        # Extrair os itens da primeira coluna (linha) e das colunas seguintes
        linhas = df.iloc[:, 0].tolist()  # A primeira coluna como índice (linha)
        colunas = df.columns.tolist()[1:]  # As demais colunas como itens de combinação
        
        return df, colunas, linhas
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar a planilha: {e}")
        return None, [], []

# Função para cruzar os itens e mostrar o valor correspondente
def cruzar_itens():
    try:
        # Pega os valores selecionados nas comboboxes
        linha_selecionada = combo_linhas.get()
        coluna_selecionada = combo_colunas.get()

        if linha_selecionada and coluna_selecionada:
            # Procurar o valor correspondente na planilha
            valor = df.loc[df.iloc[:, 0] == linha_selecionada, coluna_selecionada].values
            if valor.size > 0:
                resultado_label.config(text=f"Resultado: {valor[0]}")
            else:
                resultado_label.config(text="Valor não encontrado.")
        else:
            messagebox.showwarning("Seleção Inválida", "Selecione tanto uma linha quanto uma coluna.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao processar a consulta: {e}")

# Criar a interface gráfica com Tkinter
root = tk.Tk()
root.title("Cruzamento de Itens")

# Carregar a planilha e dados
df, colunas, linhas = carregar_planilha()

# Verificar se a planilha foi carregada corretamente
if df is not None and not df.empty:
    # Label de título
    titulo_label = tk.Label(root, text="Selecione um item da linha e da coluna:")
    titulo_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

    # ComboBox para as linhas
    combo_linhas = ttk.Combobox(root, values=linhas)
    combo_linhas.grid(row=1, column=0, padx=10, pady=10)
    
    # ComboBox para as colunas
    combo_colunas = ttk.Combobox(root, values=colunas)
    combo_colunas.grid(row=1, column=1, padx=10, pady=10)

    # Botão para realizar o cruzamento
    cruzar_button = tk.Button(root, text="Cruzar Itens", command=cruzar_itens)
    cruzar_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Label para exibir o resultado
    resultado_label = tk.Label(root, text="Resultado:")
    resultado_label.grid(row=3, column=0, columnspan=2, pady=10)

else:
    messagebox.showerror("Erro", "Planilha não carregada corretamente.")

# Rodar a aplicação
root.mainloop()