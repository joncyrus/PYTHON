import tkinter as tk

def calcular_media():
    nota1 = float(entry_nota1.get())
    nota2 = float(entry_nota2.get())
    nota3 = float(entry_nota3.get())
    
    media = (nota1 + nota2 + nota3) / 3
    label_resultado.config(text=f"Média: {media:.2f}")

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora de Média")

# Criando e posicionando os elementos na janela
label_nota1 = tk.Label(root, text="Nota 1:")
label_nota1.pack()

entry_nota1 = tk.Entry(root)
entry_nota1.pack()

label_nota2 = tk.Label(root, text="Nota 2:")
label_nota2.pack()

entry_nota2 = tk.Entry(root)
entry_nota2.pack()

label_nota3 = tk.Label(root, text="Nota 3:")
label_nota3.pack()

entry_nota3 = tk.Entry(root)
entry_nota3.pack()

botao_calcular = tk.Button(root, text="Calcular Média", command=calcular_media)
botao_calcular.pack()

label_resultado = tk.Label(root, text="")
label_resultado.pack()

# Iniciando o loop principal da interface gráfica
root.mainloop()
