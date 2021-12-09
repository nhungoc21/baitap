def diemtrungbinh(dsdiem, dstinchi):
    tongdiem = sum(dsdiem)
    tongtinchi = sum(dstinchi)
    a = len(dstinchi)
    diemtb = (tongdiem * a) / tongtinchi
    return diemtb


def diemtong(tb, diemrl):
    tong = tb + (diemrl * 0.2)
    return round(tong, 1)


diemhb = float(input('Nhap diem xet hoc bong: '))
N = int(input('Nhap so hoc sinh:'))
dshocsinh = []
dstenmon = ['Toán', 'Lập trình', 'Giới thiệu ngành']  # , 'Tư tưởng', 'Lý luận','Vi mô','QHQT','Xã hội']
dstinchi = [3, 3, 2]  # , 2, 3, 3, 2, 2]
dstong = []
dsnhanhb = []
sinhvien = []

for i in range(N):
    # Nhap ten
    ten = input('Nhap ten hoc sinh:')
    dshocsinh.append(ten)
    # Nhap diem tung mon cho 1 ban
    dsdiem = []
    for i in range(len(dstenmon)):
        print('Nhap diem mon ' + dstenmon[i])
        s = float(input())
        dsdiem.append(s)
    # Nhap drl cho 1 ban
    diemrl = int(input('Nhap drl: '))

    # Tinh diem
    diemtb = diemtrungbinh(dsdiem, dstinchi)
    tong = diemtong(diemtb, diemrl)
    dstong.append(tong)
print('Danh sach ten hoc sinh', dshocsinh)
print('Danh sach diem tong tung hoc sinh', dstong)

# Sap xep danh sach
tong_sapxep = sorted(dstong, reverse=True)
print(tong_sapxep)
for diem in tong_sapxep:
    vt = dstong.index(diem)
    sinhvien.append(dshocsinh[vt])
print(sinhvien)

# Lay ra hoc sinh nhan hoc bong
for i in range(3):
    if (tong_sapxep[i] >= diemhb):
        dsnhanhb.append(i)
for i in range(len(dsnhanhb)):
    print('Danh sach sinh vien nhan hoc bong: ' + sinhvien[dsnhanhb[i]])
