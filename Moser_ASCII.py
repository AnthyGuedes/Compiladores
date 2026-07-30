# =========================================================
# 1. TABELA DE SÍMBOLOS (Dicionário Morse -> ASCII)
# =========================================================
MORSE_PARA_ASCII = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
    '...--': '3', '....-': '4', '.....': '5', '-....': '6',
    '--...': '7', '---..': '8', '----.': '9'
}

# =========================================================
# 2. FUNÇÃO DE TRADUÇÃO (O "Scanner / Analisador Léxico")
# =========================================================
def traduzir_morse(texto_morse):
    # Separa o texto em PALAVRAS usando 2 espaços como delimitador
    palavras_morse = texto_morse.strip().split('  ')
    palavras_traduzidas = []

    for palavra in palavras_morse:
        # Separa a palavra em LETRAS (tokens) usando 1 espaço
        letras_morse = palavra.split(' ')
        
        # Converte cada token Morse para seu caractere ASCII correspondente
        # O .get(token, '?') evita erros se o usuário digitar algo inválido
        letras_ascii = [MORSE_PARA_ASCII.get(token, '?') for token in letras_morse if token]
        
        # Junta os caracteres para formar a palavra traduzida
        palavras_traduzidas.append(''.join(letras_ascii))

    # Junta as palavras traduzidas com espaço simples
    return ' '.join(palavras_traduzidas)


# =========================================================
# 3. EXECUÇÃO / TESTE
# =========================================================
if __name__ == "__main__":
    # Exemplo: SOS (3 espaços no meio para separar palavras: "SOS AH")
    entrada_morse = ".. --- ...  .- ."
    
    resultado = traduzir_morse(entrada_morse)
    
    print(f"Entrada Morse: {entrada_morse}")
    print(f"Saída ASCII  : {resultado}")