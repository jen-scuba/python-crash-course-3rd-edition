import cities as c
from f_pizza import make_pizza
from printing_functions import print_models, show_completed_models


c.describe_city("New York")
c.describe_city("Londan", "United Kingdom")
c.describe_city("Heidleburg", "Germany")

make_pizza("pineapple", "ham", "onion")
make_pizza("quatro formagi")

designs = ["dolphin", "scuba diving boat", "coral reef"]
completed = []

print_models(designs, completed)
show_completed_models(completed)