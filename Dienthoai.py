
dsdt = ['ip13', 'ip13pro', 'ip13promax', 'ip13mini']
dsgia = [2000, 3000, 5000, 500]
dssl = []
dsdoanhthu = []
listgia = []
while True: 
    loai = int(input('Nhap loai dien thoai:\n1. IPhone 13\n2. IPhone 13 Pro\n3. IPhone 13 Pro Max\n4. IPhone 13 Mini\n'))
    listgia.append(dsgia[loai - 1])
    sl = int(input('Nhap so luong: '))
    dssl.append(sl)
    t = input('Nhap tiep?(co/khong) ')
    if t == 'khong':
        break  
#lay gia
print(listgia)
print(dssl)
for i in range(len(dssl)):
    tong = dssl[i]*listgia[i]
    dsdoanhthu.append(tong)
    tongdoanhthu=sum(dsdoanhthu)
print('Doanh thu cuoi ngay: ',tongdoanhthu)