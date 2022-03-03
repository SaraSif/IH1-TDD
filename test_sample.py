from sample import fizzbuzz

def test_fizzbuzz_with_divisable_1():
    assert fizzbuzz(15) == "FizzBuzz"

def test_fizzbuzz_with_divisable_2():
    assert fizzbuzz(30) == "FizzBuzz"

def test_fizzbuzz_with_divisable_3():
    assert fizzbuzz(-60) == "FizzBuzz"

def test_buzz_with_divisable_1():
    assert fizzbuzz(5) == "Buzz"

def test_buzz_with_divisable_1():
    assert fizzbuzz(10) == "Buzz"

def test_buzz_with_divisable_1():
    assert fizzbuzz(-20) == "Buzz"
