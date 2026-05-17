# shortener.py
import string
import random
from db import get_connection


def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


def shorten_url(original_url):
    conn = get_connection()
    cursor = conn.cursor()

    # Ensure unique short code (no collisions)
    while True:
        short_code = generate_code()

        cursor.execute(
            "SELECT 1 FROM urls WHERE short_code = ?",
            (short_code,)
        )

        if not cursor.fetchone():
            break

    # store in DB
    cursor.execute(
        "INSERT INTO urls (short_code, original_url) VALUES (?, ?)",
        (short_code, original_url)
    )

    conn.commit()
    conn.close()

    return short_code


def expand_url(short_code):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT original_url FROM urls WHERE short_code = ?",
        (short_code,)
    )

    result = cursor.fetchone()
    conn.close()

    return result[0] if result else None
