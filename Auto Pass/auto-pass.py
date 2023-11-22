import hashlib
import random
import string

def generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars):
    characters = ""
    
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        print("Lütfen en az bir karakter setini seçin.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    return password, hashed_password

def main():
    print("Auto-Pass - ByFelez")

    length = int(input("Şifre uzunluğu: "))
    use_lowercase = input("Küçük harfleri kullanmak ister misiniz? (e/h): ").lower() == 'e'
    use_uppercase = input("Büyük harfleri kullanmak ister misiniz? (e/h): ").lower() == 'e'
    use_digits = input("Rakamları kullanmak ister misiniz? (e/h): ").lower() == 'e'
    use_special_chars = input("Özel karakterleri kullanmak ister misiniz? (e/h): ").lower() == 'e'

    result = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars)

    if result:
        password, hashed_password = result
        print("\nOluşturulan Şifre:", password)
        print("Şifrenin SHA-256 İle Şifrelenmiş Hali:", hashed_password)

if __name__ == "__main__":
    main()