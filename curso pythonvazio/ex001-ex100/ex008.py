m=int(input('uma distancia em metros:'))
km=m/1.000
hm=m/100
dam=m/10
dm=m*10
cent= m*100
mm= m*1.000
print('A distancia em metros {} corresponde a {}km'
'{}hm'
'{}dam'
'{}cent'
'{}mm'.format(km, hm, dam, dm, cent, mm))