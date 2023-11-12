print ("Ordinal Number")
print("Ketik 0 untuk menghentikan program")

def ordinal_number(num):
    if 10 <= num % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(num % 10, 'th')
    
    return f"{num}{suffix}"

def main():
    try:
        while True:
            num = int(input("Masukan Angka : "))
            
            
            if num == 0:
                print("Terimakasih telah menggunakan program saya.")
                break
            
            result = ordinal_number(num)
            print(result)
    except ValueError:
        print("Input harus berupa angka.")

if __name__ == "__main__":
    main()
