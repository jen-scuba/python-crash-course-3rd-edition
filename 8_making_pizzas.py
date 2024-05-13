import f_pizza

f_pizza.make_pizza(16, "pepperoni")
f_pizza.make_pizza(12, "mushrooms", "green peppers", "exrta cheese")

# option 2
import from f_pizza make_pizza

make_pizza(12, "pepperoni")
make_pizza(10, "mushrooms", "green peppers", "exrta cheese")


# option 3
import from f_pizza make_pizza as mp

mp(12, "pepperoni")
mp(10, "mushrooms", "green peppers", "exrta cheese")

# option 4
import f_pizza as p

p.make_pizza(12, "pepperoni")
p.make_pizza(16, "mushrooms", "green peppers", "exrta cheese")