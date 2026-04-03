def doc_n_dong_dau(file_path, n):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for i in range(n):
                line = f.readline()
                if not line:
                    break
                print(line.strip())
    except FileNotFoundError:
        print("Không tìm thấy file!")
n = int(input("Nhập số dòng n cần đọc: "))
doc_n_dong_dau('FIle/demo_bai1.txt', n)
