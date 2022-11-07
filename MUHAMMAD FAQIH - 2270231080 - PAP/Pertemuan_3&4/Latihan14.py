data = "ini adalh string"
print(data)
print(type(data))

# 1. cara membuat string

#1. dengan menggunakan single quote'...'
#2. dengan menggunakan double quote"..."

data = 'Menguunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('''Halo, apa kabar?''')
print("Halo, apa kabar?")
print('Ini adalah hari jumat?')

#2.Menggunakan tanda\

#Membuat tanda'menjadi string
print('mari shalat jum\'at')
print('g\'day, ist\'t it?')

#Backlash
print("C:\\user\\Ucup")

#tab
print("ucup\botong, jadi deketan")

#Newline
print("baris pertama.\nbaris kedua.") # LF -> line feed -> unix, macos, linux

print("baris pertama.\rbaris kedua") # CR -> carriage return -> commodore, acorn, lisp

print("baris pertama.\r\nbaris kedua.") # CRLF -> line feed carriage return -> dipakai oleh windows

#3.String Literal atau raw

#HAti Hati
print('C:\nnew folder') #akan salah pathnya

#Menggunakan raw string
print(R'C:\new folder')

#multi line literal string
print("""
Nama  : Ucup
kelas : 3 SD
""")

#multiline literal string dan RAW
print(R"""
Nama    : Ucup
Kelas   : 3 SD\new normal
Website : www.ucup.com/newID
""")