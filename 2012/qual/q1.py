t = [ 0 for x in range(0, 26) ] 
used = [ 0 for x in range(0,26)]
for k in range(0,3):
    en = raw_input("")
    de = raw_input("")
    for i in range(0, len(en)):
        if en[i] == ' ':
            continue
        #print en[i], de[i], ord(en[i])-ord('a')
        t[ord(en[i])-ord('a')] = de[i]
        used[ord(de[i])-ord('a')] = 1

#for k in range(0,26):
#    if t[k] == 0:
#        t[k] = chr(ord('a') + k)
#    print chr(ord('a')+k), used[k], t[k]
t[ord('z')-ord('a')] = 'q'
t[ord('q')-ord('a')] = 'z'

n = int(raw_input(""))
for k in range(0,n):
    en = raw_input("")
    de = []
    for i in range(0, len(en)):
        if en[i] == ' ':
#            print  '',
            de.append(' ')
            continue
#        print t[ord(en[i])-ord('a')],
        de.append(t[ord(en[i])-ord('a')])
    print "Case #%d: " % (k+1) + "".join(de)

