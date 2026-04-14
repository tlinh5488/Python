from operator import index
import pandas as pd
dsHoTen = ["Nguyen Van A", "Le Thi B", "Tran Van C"]
dsCC = [9, 7, 8]
dsGK = [8.0, 6.0]
dsCK = [7.0, 8.0]
sHT = pd.Series(dsHoTen)
sCC = pd.Series(dsCC)
sGK = pd.Series(dsGK, index = [0, 2])
sCK = pd.Series(dsCK, index = [1, 2])
duLieu = {"Ho va ten":sHT, "Chuyen can": sCC, "Giua ky": sGK, "Cuoi ky": sCK}
bangDiem = pd.DataFrame(duLieu)
bangDiem = bangDiem.fillna(0)
bangDiem["DiemHP"]=bangDiem["Chuyen can"]*0.1 + bangDiem["Giua ky"]*0.2 + bangDiem["Cuoi ky"]*0.7
bangDiem["Ket qua"]=bangDiem["DiemHP"]>=4
chu = ["A" if bangDiem.iloc[i].DiemHP>=7 else "B" if bangDiem.iloc[i].DiemHP>=5 else "C" for i in range(len(bangDiem))]
bangDiem["Diemchu"]=chu
bangDat = bangDiem[bangDiem["Ket qua"]==True][["Ho va ten", "DiemHP"]]
print(bangDat)
bangSap = bangDiem.sort_values("DiemHP", ascending = False)
print("Bang diem sau khi sap")
print(bangSap)
m = max(bangDiem.DiemHP)
print(m)

