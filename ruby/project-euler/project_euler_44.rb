def check_sum a, b
  return false if ((a == 0) || (b == 0))
  pent_a = pentagon a
  pent_b = pentagon b
  sum = pent_a + pent_b

  pentagon? sum
end


def try y
  x = (y*y - 1)/12

  for rhs in 1..x
    next if (x % rhs != 0) || (rhs % 3 != 2)
    diff = x/rhs
    sum = (rhs + 1)/3
    next if sum <= diff

    a = (sum + diff)/2
    b = (sum - diff)/2
    if check_sum(a, b)
      puts x/2
      puts a
      puts b
      puts pentagon(a) + pentagon(b)
      return true
    end
  end
  return false
end

#k = 0
#while true do
#  k += 6
#  if try k - 1
#    puts k - 1
#    break
#  end
#end

def index a
  (Math.sqrt(24*a + 1) + 1).to_i/6
end

max = 2400
$a = (1..max).map { |a| a * (3 * a -1)/2 }
b = $a.map { |i| index i }
puts (1..max).to_a == b

def pentagon i
  $a[i - 1]
end

def pentagon? a
  return false if a == 0
  test = pentagon index a
  test == a
end

puts pentagon 4
puts pentagon? 12
puts pentagon? 13

puts Time.new
i = 1
catch :end do
  while (i < max)
#  puts i
    j = i + 1
    while j < max
      pen_i = pentagon i
      pen_j = pentagon j
      sum = pen_i + pen_j
      diff = pen_j - pen_i
      if (pentagon?(sum) && pentagon?(diff))
        puts "#{diff}, #{pen_i} , #{pen_j} , #{sum}"
        puts "#{i}, #{j}"
        throw :end
      end
      j += 1
    end
    i += 1
  end
end
puts Time.new

require 'set'

def pentag_pair(max)
  p = []
  1.upto(max) do |n|
    pentag = n * (3 * n - 1) / 2
    (pentag > max) ? break : p << pentag
  end
  ps = Set.new(p)
  p.each {|i| p.each {|j| return (i - j).abs if ps.include?(i + j) && ps.include?((i - j).abs) }}
end
puts Time.new
puts pentag_pair(1e7)
puts Time.new