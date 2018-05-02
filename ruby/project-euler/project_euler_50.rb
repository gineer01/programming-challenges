require 'my_prime'

def find limit
  sieve = Prime::ProjectEuler27.new limit
  a = (1..limit).select { |i| sieve.is_prime i }

  max = 0
  max_prime = 0

  a.each_index do |i|
#    puts i
    j = 1
    sum = a[i]
    while (i + j < a.size)
      sum += a[i+j]
      break if sum > limit
      if (j > max) && (sieve.is_prime sum)
        max = j
        max_prime = sum
      end
      j += 1
    end
  end
  return max_prime
end

puts Time.new
puts find 1_000_000
puts Time.new


