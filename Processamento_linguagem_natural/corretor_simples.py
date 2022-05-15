from nltk import tokenize
from nltk.metrics import distance

#Abre arquivo txt contendo o dicionario BR
#LINK: https://www.ime.usp.br/~pf/dicios/br-utf8.txt
ref_arquivo = open('br-utf8.txt')
palavrasBR = ref_arquivo.read()

#lista com todas as palavras em minuscula
listaPalavrasBR_Original = re.findall(r'\w+', palavrasBR.lower())

def palavrasSimilares(palavra):
  listaPalavrasBR = listaPalavrasBR_Original.copy()
  if palavra in listaPalavrasBR:
    return [palavra]
  else:
    minDist = 99999999
    palavrasEncontradas = []
    for palavraDicionario in listaPalavrasBR:
      d = distance.edit_distance(palavra, palavraDicionario, transpositions=True)
      if(d < minDist):
        minDist = d
        palavrasEncontradas = []
        palavrasEncontradas.append(palavraDicionario)
      elif(d == minDist):
        palavrasEncontradas.append(palavraDicionario)

    return palavrasEncontradas


#TEXTO PARA SER ANALISADO
texto = "text corretr ortografico. dicionario"
texto = texto.lower()

sentences = tokenize.sent_tokenize(texto, language='portuguese')
print("Texto tokenizado em frases:\n", sentences, '\n')


#Itera sobre as sentenças e tokeniza as palavras de cada
sentences_tokenizadas = []
for sentence in sentences:
  sentences_tokenizadas.append(tokenize.word_tokenize(sentence, language='portuguese'))

print("Frases separadas em lista, com suas palavras tokenizadas:\n", sentences_tokenizadas, "\n")

#Itera sobre cada palavra em cada frase
#Aplicando a consulta de palavras similares
for i in range(len(sentences_tokenizadas)):
  for j in range(len(sentences_tokenizadas[i])):
    word = sentences_tokenizadas[i][j]
    if len(word) > 1:
      word_similares = palavrasSimilares(word)
      if len(word_similares) > 0:
        print('Palavra incorreta na frase: ', sentences[i],
              '\nPalavra :', word, ' | Sugestões: ', word_similares, '\n')
