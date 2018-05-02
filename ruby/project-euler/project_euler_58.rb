require 'prime'
require 'set'

puts Time.new

def lower_left n
  1 + 4*n*n + 2*n
end

def upper_right n
  1 - 2*n + 4 * n * n
end

def upper_left n
  1 + 4*n*n
end

#sieve = Prime::Sieve.new 700_000_000
$primes = Prime.instance.each(1_000_000).to_a

def is_prime n
  math_sqrt = Math.sqrt(n)
  $primes.each do |prime|
    return false if n % prime == 0
    break if prime > math_sqrt
  end
  true
end

step = 1
count = 3
total = 5
ratio = count*100.0/total

begin
while ratio >= 10.00
  step += 1
  total += 4
  count += 1 if is_prime lower_left(step)
#  puts lower_left(step)
  count += 1 if is_prime upper_right(step)
#  puts upper_right(step)
  count += 1 if is_prime upper_left(step)
#  puts upper_left(step)
  ratio = count*100.0/total
end
rescue => ex
  puts "step : #{step} \n Ratio : #{ratio}"
  puts ex
end

puts "Step : #{step} \n Side: #{2*step + 1} \n Ratio: #{ratio} \n Count: #{count} \n Total: #{total}"
puts Time.new