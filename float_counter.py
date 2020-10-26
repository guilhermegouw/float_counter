def main():
    text = "0,01 X 1(0,55) X 5 METROS (0,905) x 5,67 MTRS (9,0)MTRS"
    return extract_values(split_string(text=text))


def split_string(text):
    text = text.replace("x", "X")
    return text.split(sep=" X ")


def extract_values(val_list):
    val_list = [val.replace(',', '.') for val in val_list]
    val_list = [float(val[val.find("(")+1:val.find(")")]) if '(' in val else float(val) for val in val_list]
    return val_list


if __name__ == '__main__':
    print(main())