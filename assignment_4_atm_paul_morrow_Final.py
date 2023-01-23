#ATM Test Program

print('\nATM - Account Balance\n')

counter = 0

while counter < 3:

    try:
        pin = int(input('Please enter your PIN: ') or 0)

    except ValueError:

        print('PIN must be a number. Please try again.\n')
        counter += 1
        continue

    if pin != 1234:

        counter += 1
        print('Invalid PIN. Please try again.\n')
        continue
    else:

        print('\nAccount Balance $200. Goodbye.')
        break
else:
    print('\nAccount Locked. The police are on their way.')
