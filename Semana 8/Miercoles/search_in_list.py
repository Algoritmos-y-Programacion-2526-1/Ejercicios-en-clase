

def search_list(lista, element, index):
    if lista[index] == element:
        return element
    if index == len(lista) - 1:
        return None
    return search_list(lista, element, index + 1)


def main():
    lista = [1,2,45,5,7,9,6,20]
    element = int(input("Element to find:"))
    element_found = search_list(lista, element, 0)
    if element_found:
        print(f"The element is present {element}")
    else:
        print(f"The element {element} is not present ")

main()