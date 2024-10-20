import random

"""
List of characters to be used for BearcatII system.
"""
characters = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]


def get_character_from_index(index: int) -> str:
    """
    Finds the character at index in the BearcatII system.

    Args:
        index (int): Index of the character.

    Returns:
        str: Character at index.

    Raises:
        IndexError: If the index is out of the range of the BearcatII system.
    """

    if index > len(characters):
        raise IndexError("Index out of range of BearcatII system.")

    return characters[index - 1]


def get_index_from_character(character: str) -> int:
    """
    Finds the index of given character in the BearcatII system.

    Args:
        character (str): The character for which the index is to be found.

    Returns:
        int: Index of the character.

    Raises:
        Exception: If the character does not exist in the BearcatII system.
    """

    for index in range(len(characters)):
        if characters[index] == character:
            return index + 1

    raise Exception("Character not found")


def get_random_int_between(a: int, b: int) -> int:
    """
    Generates a random integer between a and b (inclusive).

    Args:
        a (int): The lower range of the random integer.
        b (int): The upper range of the random integer.

    Returns:
        int: An integer between a and b (inclusive).

    """

    return random.randint(a, b)


def euclid_gcd(a: int, b: int) -> int:
    """
    Finds the GCD of a and b based on the Euclid GCD algorithm.

    Args:
        a (int): The first number for which GCD is to be calculated.
        b (int): The second number for which GCD is to be calculated.

    Returns:
        int: The GCD of a and b.
    """

    if b == 0:
        return a

    return euclid_gcd(b, a % b)


def extended_euclid_gcd(a: int, b: int) -> tuple[int, int, int]:
    """
    Finds the GCD of a and b based on the Euclid GCD algorithm, the values of s
    and t where GCD = s * a + t * b.

    Args:
        a (int): The first number for which GCD is to be calculated.
        b (int): The second number for which GCD is to be calculated.

    Returns:
        tuple[int, int, int]: A tuple with values GCD of a and b, s and t.
    """

    if b == 0:
        return (a, 1, 0)

    (g, s, t) = extended_euclid_gcd(b, a % b)

    q = a // b

    return (g, t, s - q * t)


def powers(a: int, n: int, k: int) -> int:  # Modular Exponentiation
    """
    Calculates the value (a ^ n) mod k.

    Args:
        a (int): The base number.
        n (int): The value of the exponent.
        k (int): The value for modulation.

    Returns:
        int: Return the evaluated value for (a ^ n) mod k.

    Raises:
        ValueError: If the inverse of a and k does not exist.
    """

    if n == 0:
        return 1 % k

    if n == 1:
        return a % k

    if n < 0:
        (g, s, _) = extended_euclid_gcd(a, k)

        if g != 1:
            raise ValueError("Inverse does not exist.")

        return powers(s % k, -n, k)

    if n % 2 == 0:
        return powers((a * a) % k, int(n // 2), k)

    return (a * powers((a * a) % k, int((n - 1) // 2), k)) % k


def prime_test_miller_rabin(n: int, iterations: int) -> bool:
    """
    Checks the primality of the number n based on Miller-Rabin Primality Test.

    Args:
        n (int): The number which is to be tested for primality.
        iterations (int): The number of times the primality is to be tested to
            reduce error.

    Returns:
        bool: Returns True if n is prime else returns False.
    """

    for _ in range(iterations):
        k = n - 1

        a = get_random_int_between(2, n - 2)

        if powers(a, k, n) != 1:  # Fermat's Little Theorem
            return False

        while (k % 2) == 0:
            k = k // 2

            x = powers(a, k, n)

            if x == n - 1:
                break

            if x != 1:
                return False

    return True


def generate_n_digit_prime(n: int) -> int:
    """
    Generates an n digit prime number based on Miller-Rabin Primality Test.

    Args:
        n (int): The number of digits to be generated.

    Returns:
        int: Returns an n digit prime number.
    """

    while True:
        first_digit = str(get_random_int_between(1, 9))

        middle_digits = "".join(
            str(get_random_int_between(0, 9)) for _ in range(n - 2)
        )

        last_digit = random.choice([1, 3, 7, 9])

        prime = int(f"{first_digit}{middle_digits}{last_digit}")

        if prime_test_miller_rabin(prime, 10):
            return prime


def convert_to_bearcatii(message: str) -> list[int]:
    """
    Converts the characters of messages into a list of indexes for the character
    based on the BearcatII system.

    Args:
        message (str): The message to be converted to BearcatII system indexes.

    Returns:
        list[int]: Returns a list of BearcatII indexes corresponding to the
            characters in the message.
    """

    return [get_index_from_character(char) for char in message]


def convert_bearcatii_to_string(bearcatii: list[int]) -> str:
    """
    Converts a list of BearcatII system indexes to string.

    Args:
        bearcatii (list[int]): The list of BearcatII indexes to be converted to
            string.

    Returns:
        str: Returns a corresponding string from the list of BearcatII indexes.
    """

    return "".join([get_character_from_index(index) for index in bearcatii])


def convert_to_base_n(value: int, n: int) -> list[int]:
    """
    Converts a number to its base n form.

    Args:
        value (int): The number to be converted.
        n (int): The base the number is to be converted to.

    Returns:
        list[int]: Returns a list of integers representing the digits of the
            base-n value of the number.
    """

    output: list[int] = []

    while value:
        output.insert(0, value % n)
        value = value // n

    return output


def horner_eval(coefficients: list[int], value: int) -> int:
    """
    Evaluates a polynomial equation at x = value.

    Args:
        coefficients (list[int]): The list of coefficients of the equation in
            decreasing order of degree.
        value (int): The value at which the equation is to be evaluated.

    Returns:
        int: The output of the equation at x = value.
    """

    output: int = 0

    for coefficient in coefficients:
        output = output * value + coefficient

    return output


def euler_totient(p: int, q: int) -> int:
    """
    Calculates the value for euler totient of n based of two primes p and q
    where n = p * q.

    Args:
        p (int): The first prime number that can divide n.
        q (int): The second prime number that can divide n.

    Returns:
        int: The value of euler totient function phi(n).
    """

    return (p - 1) * (q - 1)


def rsa() -> None:
    """
    A demonstration of the RSA encryption system. It takes in a public key and
    message from the user and performs both encryption and decryption.
    """

    NUMBER_OF_DIGITS_IN_PRIME = 20

    p = generate_n_digit_prime(NUMBER_OF_DIGITS_IN_PRIME)
    q = generate_n_digit_prime(NUMBER_OF_DIGITS_IN_PRIME)
    n = p * q
    phi = euler_totient(p, q)

    while True:
        e = int(input("Enter the value for public key: "))

        if euclid_gcd(e, phi) == 1:
            break

        print("The value is not relatively prime to the euler totient value.")

    message = input("Enter the message to encrypt: ")
    message_to_bearcatii = convert_to_bearcatii(message)
    bearcatii_to_decimal = horner_eval(
        message_to_bearcatii, len(characters) + 1
    )

    C = powers(bearcatii_to_decimal, e, n)

    (_, private_key, _) = extended_euclid_gcd(e, phi)

    decrypted = powers(C, private_key, n)
    decrypted_to_bearcatii = convert_to_base_n(decrypted, len(characters) + 1)
    decrypted_message = convert_bearcatii_to_string(decrypted_to_bearcatii)

    print("p:", p)
    print("q:", q)
    print("n:", n)
    print("M:", message)
    print("C:", C)
    print("P:", decrypted_message)


rsa()
