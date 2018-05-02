require 'my_prime'
require 'set'

def repeating s, no_of_digits
  temp = Hash.new 0
  s.each_char {|i| temp[i] += 1; return i if temp[i] >= no_of_digits}
  return false
end

def find limit, no_of_digits, condition
  sieve = Prime::ProjectEuler27.new limit
  min = 10**no_of_digits
  a = (50000..limit).select { |i| i > min && sieve.is_prime(i) }

  permutations = (0..6).map {|l| (0...l).to_a.permutation(no_of_digits)}

  #for each prime, transform it and put in a hash
  a.each do |i|
    i_string = i.to_s
    l = i_string.length

    next unless repeated = repeating( i_string, no_of_digits)

    #all possible transformations
    permutations[l].each do |perm|
      s = i.to_s
      if perm.all? {|index| s[index] == repeated}
        count = 0
        b = (1..9).map do |digit|
          no_of_digits.times {|index| s[perm[index]] = "#{digit}" }
          count += 1 if sieve.is_prime s.to_i
          s.clone
        end
        return b if count >= condition
      end
    end
  end

  return nil
end

puts Time.new
result = find(1000000, 3, 8)
p result.sort if result
puts Time.new