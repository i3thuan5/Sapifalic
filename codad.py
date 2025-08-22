def read_amis_dict():
    kiatko = {}
    with open('amis-moedict-s.txt') as tong:
        for tsua in tong.readlines():
            word = tsua.strip()
            kiatko[word.replace('e', '')] = word
            kiatko[word.replace('e', '').capitalize()] = word.capitalize()
    return kiatko
