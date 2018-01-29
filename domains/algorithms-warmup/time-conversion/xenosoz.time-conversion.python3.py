s=input()
print('%02d'%(int(s[:2])%12+(s[-2]=='P')*12)+s[2:-2])
