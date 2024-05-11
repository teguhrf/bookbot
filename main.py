def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
        file_contents = file_contents.lower()

    words = file_contents.split()
    dict = count_char(words)
    new_ls = make_dict(dict)
    new_ls.sort(reverse=True, key=dict_sort)

    display_result(new_ls)

def count_char(ls):
    split_char = [char for word in ls for char in word if char.isalpha()]
    # print(split_char)

    my_dict = {}

    for i in split_char:
        if i in my_dict:
            my_dict[i] += 1
        if i not in my_dict:
            my_dict[i] = 1
    
    return my_dict


def make_dict(dict_char):
    new_list = []
    
    for i in dict_char:
        # key = i
        # value = dict_char[i]
        tmp_dict = {"char": i, "num": dict_char[i]}
        new_list.append(tmp_dict)
    
    return new_list

def dict_sort(dict):
    return dict["num"]

def display_result(ls):
    # for i in ls:
    #     for key, value in i.items():
    #         # print(f"The '{key}' character was found {value} times")
    #         print("Key:", key, "Value:", value)

    for i in ls:
        value_1 = i.get("char", "")
        value_2 = i.get("num", "")

        print(f"The '{value_1}' character was found {value_2} times")

main()
    