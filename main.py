def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = get_wc(file_contents)
        print(f"Total words: {word_count}\n")
        list = make_dict_list(get_char_dict(file_contents))
        for item in list:
            print(f"The '{item["name"]}' character was found {item["num"]} times.")
        print("\n=====End of Report=====")

def get_wc(string):
    string_array = string.split()
    return len(string_array)

def get_char_dict(string):
    chars = {}
    string = ''.join(string.split())    
    for s in string:
        s = s.lower()
        if s in chars:
            num = chars.get(s)
            chars[s] = num + 1
        else:
            chars.update({s: 1})
    return chars

def make_dict_list(dict):
    list = []
    for key in dict:
        list.append({"name":key, "num":dict[key]})
    sorted_list = list.sort(reverse=True, key=sort_on)
    return list

def sort_on(dict):
    return(dict["num"])

print("=====Generating book report=====\n")
main()