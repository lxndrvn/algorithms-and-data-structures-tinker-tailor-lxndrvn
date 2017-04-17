


def kovetkezo_gyerek(gyerekek, aktualis_gyerek):
	if aktualis_gyerek == gyerekek[-1] or aktualis_gyerek == None:
		return gyerekek[0]

	else: 
		gyerek_index = gyerekek.index(aktualis_gyerek)
		return gyerekek[gyerek_index + 1]


def szamolas(gyerekek, szotagok, aktualis_gyerek):
	for szotag in range(szotagok - 1):
		aktualis_gyerek = kovetkezo_gyerek(gyerekek, aktualis_gyerek)
	return aktualis_gyerek


def jatek(gyerekek_szama, szotagok):
	gyerekek = range(1, gyerekek_szama + 1)
	aktualis_gyerek = gyerekek[0]
	kiesett_gyerekek = []
	while len(gyerekek) > 0:
		kieso_gyerek = szamolas(gyerekek, szotagok, aktualis_gyerek)
		aktualis_gyerek = kovetkezo_gyerek(gyerekek, kieso_gyerek)
		gyerekek.remove(kieso_gyerek)
		kiesett_gyerekek.append(kieso_gyerek)
	return kiesett_gyerekek

print(jatek(5, 3))






