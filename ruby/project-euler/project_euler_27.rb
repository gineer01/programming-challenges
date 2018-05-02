# Created by IntelliJ IDEA.
# User: dongc
# Date: May 25, 2010
# Time: 5:06:43 PM
# To change this template use File | Settings | File Templates.

#Considering quadratics of the form:
#n² + an + b, where |a|  1000 and |b|  1000
#
#where |n| is the modulus/absolute value of n
#e.g. |11| = 11 and |4| = 4
#
#Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number
# of primes for consecutive values of n, starting with n = 0.

class Sieve
  def initialize bound
    @bound = bound
    @is_multiple = []
    @sqrt_of_bound = Math.sqrt(bound).to_i

    do_sieve
  end

  def is_prime? n
    if n == 1
      return false
    elsif n == 2
      return true
    elsif n % 2 == 0
      return false
    elsif n > @bound
      raise "Cannot process more than #@bound: #{n}"
    else
      return !@is_multiple[(n-1)/2]
    end

  end


  private
  def do_sieve
    index_to_stop = @sqrt_of_bound/2

    for i in 1..index_to_stop
      if (!@is_multiple[i])
        start_index = 2 * i * (i + 1)
        start_index.step(@bound/2, 2*i + 1) do |j|
          @is_multiple[j] = true;
        end
      end
    end
  end
end

def f n, a, b
  n*n  + a*n + b
end

sieve = Sieve.new 2_000_000



max = 0
max_a = nil
max_b = nil

for b in -999..999
  next if !(sieve.is_prime? b)

  for a in -999..999
    i = 0
    while (sieve.is_prime? f(i, a, b) )
      i += 1
    end

    if (i > max)
      max = i
      max_a = a
      max_b = b
    end
  end
end

p max
p max_a
p max_b
p max_a * max_b