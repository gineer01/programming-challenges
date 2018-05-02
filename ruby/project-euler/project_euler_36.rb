# Created by IntelliJ IDEA.
# User: dongc
# Date: May 25, 2010
# Time: 1:13:23 AM
# To change this template use File | Settings | File Templates.


#The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#(Please note that the palindromic number, in either base, may not include leading zeros.)

puts Time.new

count = 0
def is_panlindrome n
  n.reverse == n
end

for n in 1..1_000_000
  decimal_string = n.to_s
  if (is_panlindrome decimal_string) && (is_panlindrome n.to_s(2))
    count += n
  end
end


puts count
puts Time.new