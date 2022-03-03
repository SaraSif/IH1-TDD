def fizzbuzz(integer):
    if integer % 5 == 0 and integer % 3 == 0:
        return "FizzBuzz"
    if integer % 5 == 0 and integer % 3 != 0:
        return "Buzz"
    if integer % 5 != 0 and integer % 3 == 0:
        return "Fizz"

