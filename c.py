import binascii
character_frequencies ={
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000,
		'A': .08167, 'B': .01492, 'C': .02782, 'D': .04253,
        'E': .12702, 'F': .02228, 'G': .02015, 'H': .06094,
        'I': .06094, 'J': .00153, 'K': .00772, 'L': .04025,
        'M': .02406, 'N': .06749, 'O': .07507, 'P': .01929,
        'Q': .00095, 'R': .05987, 'S': .06327, 'T': .09056,
        'U': .02758, 'V': .00978, 'W': .02360, 'X': .00150,
        'Y': .01974, 'Z': .00074, ' ': .13000
}

def decode_line(str):
	max=0
	encoded = binascii.unhexlify(str)
	temp=''
	for xor_key in range(256):
		decoded = ''.join(chr(b ^ xor_key) for b in encoded)
		#print(decoded)
		score=0
		if decoded.isprintable():
			for char in decoded:
				if char in character_frequencies.keys():
					score += character_frequencies[char]
		#print(score)
		if(score>max):			
			max=score
			temp=decoded
	return max,temp
				
str='1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
res=""
res=decode_line(str)
print(res)