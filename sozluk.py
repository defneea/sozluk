print("sözlük uygulamasına hoşgeldiniz :D")
meme_dict = {
    "LOL" : "Sesli gülmek",
    "OK" : "tamam",
    "KNK" : "arkadaş",
    "GİTHUB" : "kodları yüklediğimiz platform"
}

while True:
    word = input("Anlamadığın kelimeyi gir")

    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("kelime yok")
        continue    

    x = input("durdurmak için q ya bas=?")

    if x == "q":
        break
