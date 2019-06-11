ch=raw_input()
vo=['a','e','i','o','u']
if ch in vo:
  print "Vowel"
else:
  if ch.isalpha:
    print "Consonant"
  else:
    print "invalid"
