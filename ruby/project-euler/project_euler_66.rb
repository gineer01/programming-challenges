# Created by IntelliJ IDEA.
# User: dongc
# Date: May 25, 2010
# Time: 10:50:59 PM
# To change this template use File | Settings | File Templates.

require 'bigdecimal'

def is_square n
  return ((Math.sqrt n).floor)**2 == n
end
def solve_pell n
  return -1 if is_square n
  n_big = BigDecimal.new n.to_s
  sqrt = BigDecimal.new (n_big.sqrt(50).to_s)

  h_n_1 = 1
  h_n_2 = 0
  k_n_1 = 0
  k_n_2 = 1

  one = BigDecimal.new "1.0"
  while true
    a = sqrt.floor.to_i
    x = a * h_n_1 + h_n_2
    y = a * k_n_1 + k_n_2

    value = x*x - n * y * y
    return x.to_i if (value == 1)

    sqrt = one / (sqrt - a)
    h_n_2 = h_n_1
    h_n_1 = x
    k_n_2 = k_n_1
    k_n_1 = y
  end
end

#p solve_pell 3
#p solve_pell 157

max = 0
for i in 200..400
  p "\nWorking on #{i} : "
  result = solve_pell i
  p max = result if result > max
end