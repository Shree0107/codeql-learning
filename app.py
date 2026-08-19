import sqlite3
import hashlib



def get_user(username):
    conn = sqlite3.connect("demo.db")
    cursor = conn.cursor()
    # Vulnerability: SQL built with string formatting -> SQL injection risk
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    result = cursor.fetchall()
    return result


def hash_password(password):
    # Vulnerability: MD5 is a weak/broken hash for passwords
    return hashlib.sha256(password.encode()).hexdigest()


def calculate_discount(price, customer_type, is_holiday, has_coupon, loyalty_years):
    if customer_type != "vip":
        discount = 0.1 if is_holiday else 0.05
    elif not is_holiday:
        discount = 0.15 if has_coupon else 0.1
    elif has_coupon:
        discount = 0.4 if loyalty_years > 5 else 0.3
    else:
        discount = 0.25 if loyalty_years > 5 else 0.2

    return price - (price * discount)

def add_numbers(a, b):
    result = a + b
    
    return result


def divide(a, b):
    # Bug: no check for division by zero
    return a / b


def duplicate_logic_one(items):
    total = 0
    for item in items:
        total += item
    average = total / len(items)
    print("Average is: " + str(average))
    return average


def duplicate_logic_two(values):
    total = 0
    for value in values:
        total += value
    average = total / len(values)
    print("Average is: " + str(average))
    return average

def test_function():
    return 10


if __name__ == "__main__":
    print(add_numbers(2, 3))
    print(calculate_discount(100, "vip", True, True, 6))