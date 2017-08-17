def readline():
	try:
		line = input()
	except:
		return None
	return line.strip()

k = -1
while True:
	k = readline()
	if k is None:
		break
	k = int(k)
	if k < 1:
		continue
	fracs = []
	for y in range(k + 1, 2 * k + 1):
		if k * y % (y - k) == 0:
			x = k * y // (y - k)
			fracs.append((x, y))
	print(len(fracs))
	for frac in fracs:
		print('1/{} = 1/{} + 1/{}'.format(k, frac[0], frac[1]))
