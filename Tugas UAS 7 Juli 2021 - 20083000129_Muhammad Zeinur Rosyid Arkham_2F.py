# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 15:02:35 2021

@author: Muhammad Zeinur Rosyid Arkham
NIM    : 20083000129
Kelas  : 2_F
Tugas  : UAS
"""
import datetime
z = datetime.datetime.now()

Ulang = "y"
while Ulang=="y" or Ulang=="Y":
    
    print("")
    print("=================================================")
    print("          SLIP GAJI KARYAWAN CV. LOGOS  ")
    print("=================================================")
    print("           tangal: " + (z.strftime("%x")))
    print("")
    print("=================================================")
    print("")

   
    Nama        = input("Masukkan Nama Karyawan                          = ")
    Gol         = input("Masukkan Jenis Golongan (ketik 1, 2, atau 3)    = ")
    if Gol=="1" or Gol==1:
        Gaji = 2500000
        GOL  ="1"
    elif Gol=="2" or Gol==2:
        Gaji = 4500000
        GOL  ="2"
    elif Gol=="3" or Gol==3:
        Gaji = 6500000
        GOL  ="3"
    else:
        Ulang = print("Golongan tidak Tersedia pada Pilihan")
        break
    
    JenK        = input("Masukkan Jenis gender (a.Laki-laki  b.Perempuan)= ")
    if JenK=="a" or JenK=="A":
        Gen = "laki-laki"
    elif JenK=="b" or JenK=="B":
        Gen = "Perempuan"
    else:
        Ulang = print("Tidak Tersedia pada Pilihan")
        break
    
    StatK       = input("Masukkan Status Kawin (a.Kawin    b.Belum Kawin)= ")
    if StatK=="a" or StatK=="A":
        sts = "Kawin"
    elif StatK=="b" or StatK=="B":
        sts = "Belum Kawin"
    else:
        Ulang = print("Tidak Tersedia pada Pilihan")
        break
    
    PA          = input("Sudah Punya Anak?   ketik y/T      = ")
    if PA=="y" or "Y":
        Sdh = "Sudah"
    else:
        Sdh = "Belum"
        
    if Gen=="laki-laki" and sts=="Kawin":
        if Gol=="1" or Gol==1:
            tuni = Gaji*0.01
        elif Gol=="2" or Gol==2:
            tuni = Gaji*0.02
        elif Gol=="3" or Gol==3:
            tuni = Gaji*0.03
    else:
        tuni = 0
    
    if PA=="y" or PA=="Y" and sts=="Kawin":
        tuna = Gaji * 0.02
    else:
        tuna = 0
    
    GB = Gaji + tuni + tuna
    BJ1 = GB * 0.005
    BJ = GB - BJ1
    IP = 15500
    IO = 3500
    GN = GB - IP - IO
    
    print("")
    print("===============================================")
    print("          SLIP GAJI KARYAWAN CV. LOGOS  ")
    print("===============================================")
    print("           Tangal: " + (z.strftime("%x")))
    print("===============================================")
    print("")
    print("==> Nama karyawan   : " + Nama)
    print("==> Gol             : " + GOL)
    print("==> Jenis Kelamin   : " + Gen)
    print("==> Status          : " + sts)
    print("==> Gaji Pokok      : Rp " + str(Gaji))
    print("==> Tunjangan Istri : Rp " + str(tuni))
    print("==> Tunjangan Anak  : Rp " + str(tuna))
    print("==>> Gaji Bruto     : Rp " + str(GB))
    print("==================================")
    print("==> Biaya Jabatan   : Rp " + str(BJ1))
    print("==> Iuran Pensiun   : Rp " + str(IP))
    print("==> Iuran Organisasi: Rp " + str(IO))
    print("==>> Gaji Neto      : Rp " + str(GN))

    Ulang = input(">> Hitung Gaji lain ? y/t = ")
    if Ulang=="t" or Ulang=="T":
        break
    
            
        
        
        
        
        
        