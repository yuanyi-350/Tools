import pikepdf


def main():
    book_name = input()

    if book_name[0] == '"':
        book_name = book_name[1:-1]

    with pikepdf.open(book_name) as pdf:
        if "/Outlines" in pdf.Root:
            del pdf.Root["/Outlines"]
        save_place = book_name[:-4] + "-new.pdf"
        pdf.save(save_place)
        print(f"Save to {save_place}")


if __name__ == '__main__':
    main()
