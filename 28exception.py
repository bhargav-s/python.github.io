while True:
    try:
        number = int(input("whats your answer?"))
        print(18/number)
        break
    except ValueError:
        print("Enter Correct Input")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    finally:
        print("code Excecuted Successfully")