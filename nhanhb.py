def nhap_diem_mon(dstenmon):
    dsdiem = []
    for i in range(len(dstenmon)):
        print('Nhap diem mon ' + dstenmon[i])
        s = float(input())
        dsdiem.append(s)
    return dsdiem

def tinhdiem(dsdiem, dstinchi, diemrl):
    tongdiem = sum(dsdiem)
    tongtinchi = sum(dstinchi)
    a = len(dstinchi)
    diemtb = (tongdiem * a) / tongtinchi
    tong = diemtb + (diemrl * 0.2)
    return round(tong, 1)

def sapxepten(tong_sapxep, dstong, dshocsinh):
    sinhvien = []
    for diem in tong_sapxep:
        vt = dstong.index(diem)
        sinhvien.append(dshocsinh[vt])
    return sinhvien

diemhb = float(input('Nhap diem xet hoc bong: '))
N = int(input('Nhap so hoc sinh:'))
dstenmon = ['Toán', 'Lập trình', 'Giới thiệu ngành']  # , 'Tư tưởng', 'Lý luận','Vi mô','QHQT','Xã hội']
dstinchi = [3, 3, 2]  # , 2, 3, 3, 2, 2]
dshocsinh = []
dstong = []
dsnhanhb = []

for i in range(N):
    ten = input('Nhap ten hoc sinh:')
    dshocsinh.append(ten)
    dsdiem = nhap_diem_mon(dstenmon)
    diemrl = int(input('Nhap drl: '))

    # Tinh diem
    tong = tinhdiem(dsdiem, dstinchi, diemrl)
    dstong.append(tong)

# Sap xep danh sach
tong_sapxep = sorted(dstong, reverse=True)
sinhvien = sapxepten(tong_sapxep, dstong, dshocsinh)

# Lay ra hoc sinh nhan hoc bong
for i in range(3):
    if (tong_sapxep[i] >= diemhb):
        dsnhanhb.append(i)
    else: 
        print('Khong co hoc sinh du dieu kien')
        break
for i in range(len(dsnhanhb)):
    print('Danh sach sinh vien nhan hoc bong: ' + sinhvien[dsnhanhb[i]])
