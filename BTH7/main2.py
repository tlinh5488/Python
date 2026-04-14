import pandas as pd

data = {
    "HoTen": ["Nguyen Van A", "Tran Thi B", "Le Van C", "Pham Thi D"],
    "NamSinh": [2005, 1990, 1970, 1960],
    "Email": ["a@gmail.com", "b@gmail.com", "c@gmail.com", "d@gmail.com"],
    "SDT": ["0123", "0456", "0789", "0111"]
}

df = pd.DataFrame(data)
current_year = 2026
df["Tuoi"] = current_year - df["NamSinh"]
def phan_loai(tuoi):
    if tuoi < 35:
        return "Trẻ"
    elif tuoi < 60:
        return "Trung niên"
    else:
        return "Cao niên"
df["PhanLoai"] = df["Tuoi"].apply(phan_loai)
cao_nien = df[df["PhanLoai"] == "Cao niên"]
ds_ht_sdt = df[["HoTen", "SDT"]]
ten = input("Nhap ho ten can tim: ").strip()
ket_qua = df[df["HoTen"].str.lower() == ten.lower()]
if not ket_qua.empty:
    print("So dien thoai:", ket_qua["SDT"].values[0])
else:
    print("Khong tim thay trong danh sach")

df_sorted = df.sort_values(by="Tuoi")

df_final = df.drop(columns=["Tuoi", "PhanLoai"])

print("\n=== DANH SACH BAN DAU ===")
print(df)

print("\n=== DANH SACH CAO NIEN ===")
print(cao_nien)

print("\n=== HO TEN + SDT ===")
print(ds_ht_sdt)

print("\n=== SAP XEP THEO TUOI ===")
print(df_sorted)

print("\n=== SAU KHI XOA COT ===")
print(df_final)