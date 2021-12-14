#Ung Thị Như Ngọc - K214060404

def tinh_doanh_thu(dssl, gia_dt_daban):
    dsdoanhthu = []
    for i in range(len(dssl)):
        tong = dssl[i]*gia_dt_daban[i]
        dsdoanhthu.append(tong)
    return dsdoanhthu

dsdt = ['ip13', 'ip13pro', 'ip13promax', 'ip13mini']
dsgia = [2000, 3000, 5000, 500]
dssl = []
gia_dt_daban = []
#Nhap 
while True: 
    try: 
        loai = int(input('1. IPhone 13\n2. IPhone 13 Pro\n3. IPhone 13 Pro Max\n4. IPhone 13 Mini\nNhap so tuong ung loai dien thoai: '))
        gia_dt_daban.append(dsgia[loai - 1])
        sl = int(input('Nhap so luong: '))
        dssl.append(sl)
        t = input('Nhap tiep?(co/khong) ')
        if t == 'khong':
            break  
    except:
        print ('Hay nhap dung so')
#Tinh doanh thu
dsdoanhthu=tinh_doanh_thu(dssl,gia_dt_daban)
tongdoanhthu=sum(dsdoanhthu)
print('Doanh thu cuoi ngay: ',tongdoanhthu)