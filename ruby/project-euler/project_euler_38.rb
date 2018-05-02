# Created by IntelliJ IDEA.
# User: dongc
# Date: May 25, 2010
# Time: 9:53:09 PM
# To change this template use File | Settings | File Templates.

def concat_product n, array
  result = ""
  array.each do |i|
    result += (i*n).to_s
  end

  return result.to_i
end

def is_pandigital n
  check = []
  while n > 0
    return false if check[n % 10]
    check[n % 10] = true
    n /= 10
  end

  return false if check[0]

  for i in 1..9
    return false if !check[i]
  end

  return true
end

#puts is_pandigital concat_product 9, [1, 2, 3, 4, 5]
#puts is_pandigital concat_product 192, [1, 2, 3]

array = [1]
max = 0
for i in 2..9
  array<< i

  upper = 10**(9/i + 1)
  lower = 10**(9/i)/9
  for n in lower..upper
    if is_pandigital concat_product n, array
      p array, n, concat_product(n, array) if (concat_product n, array) >  918273645  
    end
  end

end