#Ung Thị Như Ngọc - K214060404

# tinh diem tong tung khoi
def tongdiem(a, b, c, dstongdiem):
    tong = a * 2 + b + c
    dstongdiem.append(tong)
    return dstongdiem

# nhap diem tung mon
dsdiem = []
dstenmon = ['Toan', 'Ly', 'Hoa', 'Sinh', 'Su', 'Dia', 'Van', 'Anh']
for i in range(len(dstenmon)):
    print('Nhap diem ' + dstenmon[i])
    s = float(input())
    dsdiem.append(s)
print('Danh sach diem tung mon: ', dsdiem)

# tong diem tung khoi
dstongdiem = []
tongdiem(dsdiem[0], dsdiem[1], dsdiem[2], dstongdiem)
tongdiem(dsdiem[3], dsdiem[2], dsdiem[0], dstongdiem)
tongdiem(dsdiem[6], dsdiem[4], dsdiem[5], dstongdiem)
tongdiem(dsdiem[7], dsdiem[0], dsdiem[6], dstongdiem)
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
