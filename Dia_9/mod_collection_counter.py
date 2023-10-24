from collections import Counter

frase = "al pan pan y al vino vino"
print(Counter(frase.split()))

serie = Counter([1,6,5,3,6,5,4,3,3,3,7,8,1,6])
print(serie.most_common(1))
print(list(serie))