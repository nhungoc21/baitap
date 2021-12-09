
dsdt = ['ip13', 'ip13pro', 'ip13promax', 'ip13mini']
dsgia = [2000, 3000, 5000, 500]
dssl = []
dsdoanhthu = []
vitri = []
listgia = []
while True: 
    loai = input('Nhap loai dien thoai: ')
    sl = int(input('Nhap so luong: '))
    dssl.append(sl)
    #lay vi tri
    for dt in dsdt:
        if dt == loai:
            vt=dsdt.index(dt)
            vitri.append(vt)
    print(vitri)
    
    t = input('Nhap tiep?(co/khong) ')
    if t == 'khong':
        break  
#lay gia
for i in range(len(vitri)):
    listgia.append(dsgia[vitri[i]])
print(listgia)
print(dssl)
for i in range(len(dssl)):
    tong = dssl[i]*listgia[i]
    dsdoanhthu.append(tong)
    tongdoanhthu=sum(dsdoanhthu)
print('Doanh thu cuoi ngay: ',tongdoanhthu)