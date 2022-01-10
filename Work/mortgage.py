# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000



while principal > 0:
    month += 1
    extra_payment = 0
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        extra_payment += 1000
        print(month)
    principal = principal * (1+rate/12) - payment - extra_payment
    total_paid = total_paid + payment
    print(f'{month} {total_paid:0.2f} {principal:0.2f}')


print(f'Total paid: {total_paid} in {month} months')
