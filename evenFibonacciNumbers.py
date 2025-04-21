
fn_2 = 0
fn_1 = 1
fn = 1
sum_even = 0
while fn_1 <= 4000000:
    if fn_1 % 2 == 0:
        sum_even = sum_even + fn_1
    fn_2 = fn_1
    fn_1 = fn
    fn = fn_1 + fn_2
print(sum_even)
