#Ung Thị Như Ngọc - K214060404

def nhap_diem_mon(dstenmon):
    dsdiem = []
    for i in range(len(dstenmon)):
        print('Nhap diem mon ' + dstenmon[i])
        s = float(input())
        dsdiem.append(s)
    return dsdiem

def tinhdiem(dsdiem, dstinchi, diemrl):
    ds_diem_mon = []
    for i in range(len(dstinchi)):
        diem_mon_hoc = dstinchi[i] * dsdiem[i]  
        ds_diem_mon.append(diem_mon_hoc)
    tong_diem_mon = sum(ds_diem_mon)
    tongtinchi = sum(dstinchi)
    tong = (tong_diem_mon / tongtinchi) + (diemrl * 0.2)
    return round(tong, 1)

def sapxepten(tong_sapxep, dstong, dstensv):
    ten_sapxep = []
    for diem in tong_sapxep:
        vt = dstong.index(diem)
        ten_sapxep.append(dstensv[vt])
    return ten_sapxep

dstenmon = ['Toan cao cap', 'Lap trinh', 'GTN', 'Tu tuong', 'Ly luan','Vi mo','QHQT','Xa hoi']
dstinchi = [3, 3, 2, 2, 3, 3, 2, 2]
dstensv = []
dstong = []

#Nhap ten va diem
diemhb = float(input('Nhap diem xet hoc bong: '))
N = int(input('Nhap so hoc sinh: '))
for i in range(N):
    ten = input('Nhap ten hoc sinh: ')
    dstensv.append(ten)
    dsdiem = nhap_diem_mon(dstenmon)
    diemrl = int(input('Nhap drl: '))

    # Tinh diem
    tong = tinhdiem(dsdiem, dstinchi, diemrl)
    dstong.append(tong)

# Sap xep danh sach
tong_sapxep = sorted(dstong, reverse=True)
ten_sapxep = sapxepten(tong_sapxep, dstong, dstensv)

# Lay ra hoc sinh nhan hoc bong
dsvitri = []
ds_sinhvien = []
for i in range(5):
    if (tong_sapxep[i] >= diemhb):
        dsvitri.append(i)
for i in range(len(dsvitri)):
    ds_sinhvien.append(ten_sapxep[dsvitri[i]])
print('Danh sach sinh vien nhan hoc bong: ', ", ".join(ds_sinhvien))
