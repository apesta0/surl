# main.py
from db import init_db
from shortener import shorten_url, expand_url


def run():
    init_db()

    while True:
        print("\n--- URL Shortener ---")
        print("1. Shorten URL")
        print("2. Expand URL")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            url = input("Enter URL: ")
            code = shorten_url(url)
            print("Short code:", code)

        elif choice == "2":
            code = input("Enter short code: ")
            url = expand_url(code)

            if url:
                print("Original URL:", url)
            else:
                print("Not found")

        elif choice == "3":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    run()
