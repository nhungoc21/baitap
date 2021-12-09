dsdiem = []
dstongdiem = []
# nhapdiem
dstenmon = ['Toan', 'Ly', 'Hoa', 'Sinh', 'Su', 'Dia', 'Van', 'Anh']
for i in range(len(dstenmon)):
    print('Nhapmon ' + dstenmon[i])
    s = float(input())
    dsdiem.append(s)
print('Danh sach diem tung mon: ', dsdiem)

# tinhdiem
def tongdiem(a, b, c):
    tong = a * 2 + b + c
    dstongdiem.append(tong)
    return dstongdiem

# tong tung khoi
tongdiem(dsdiem[0], dsdiem[1], dsdiem[2])
tongdiem(dsdiem[3], dsdiem[2], dsdiem[0])
tongdiem(dsdiem[6], dsdiem[4], dsdiem[5])
tongdiem(dsdiem[7], dsdiem[0], dsdiem[6])
print('Danh sach tong diem theo khoi: ', dstongdiem)

# tuvan
diem_lon_nhat = max(dstongdiem)
dsvitri = []
for vt in range(len(dstongdiem)):
    if dstongdiem[vt] == diem_lon_nhat:
        dsvitri.append(vt)
dstohop = ['A', 'B', 'C', 'D']
for i in range(len(dsvitri)):
    print('Ban nen chon khoi: ' + dstohop[dsvitri[i]])
