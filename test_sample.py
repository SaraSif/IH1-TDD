from sample import fizzbuzz

def test_fizzbuzz_with_divisable_1():
    assert fizzbuzz(15) == "FizzBuzz"

def test_fizzbuzz_with_divisable_2():
    assert fizzbuzz(30) == "FizzBuzz"

def test_fizzbuzz_with_divisable_3():
    assert fizzbuzz(-60) == "FizzBuzz"
