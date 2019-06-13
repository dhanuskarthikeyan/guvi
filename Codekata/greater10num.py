ad=raw_input()
if len(ad) == 1:
	print("10")
else:
    print(str(int(ad[0:len(ad)-1])+1) + "0")
