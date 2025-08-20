import re


_sapicacawas = re.compile('(ng|ey|.)')
vowel = ['a', 'e', 'i', 'o', 'ey']

def bible2ilrdf(bible):
    kiatko = []
    for word in bible.split():
        kiatko.append(bible2ilrdf_word(word))
    return ' '.join(kiatko)

def bible2ilrdf_word(bible):
    im = _sapicacawas.findall(bible)
    kiatko = [im[0]]
    poo_e = True
    for tsing, au in zip(im, im[1:]):
        if tsing in vowel or au in vowel:
            poo_e = False
        if poo_e:
            kiatko.append('e')
        kiatko.append(au)
    return ''.join(kiatko)
