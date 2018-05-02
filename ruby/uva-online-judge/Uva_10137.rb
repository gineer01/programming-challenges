# Created by IntelliJ IDEA.
# User: dongc
# Date: Jun 21, 2010
# Time: 5:28:56 PM
# To change this template use File | Settings | File Templates.
require 'bigdecimal'

def solve amounts, n
  sum = amounts.inject{|s, amount| s + amount}
  average = sum / n
  remainder = sum % n
  count = 0
  exchange = amounts.inject(0) do |e, amount|
    count += 1 if amount > average
    e + ((amount > average) ? amount - average : 0)
  end
  exchange - ((count < remainder)?count:remainder)
end

puts Time.new
File.open "UVa_10137.input" do |f|
  while (n = f.gets.to_i) != 0
    amounts = []
    n.times do
      s = BigDecimal.new f.gets
      amounts << (s * 100).to_i
    end

    printf("$%.2f\n", solve(amounts, n) / 100.0)
  end
end

puts Time.new