# Created by IntelliJ IDEA.
# User: dongc
# Date: May 23, 2010
# Time: 3:36:55 AM
# To change this template use File | Settings | File Templates.
def run_tests
  File.open "output_CB.txt", "w" do |output|
    File.open "B-large-practice.in" do |input|
      number_of_tests = input.gets.to_i
      number_of_tests.times do |test_number|

        test = input.gets.chomp.split /\s+/, 3

        l = test[0].to_i
        p = test[1].to_i
        c = test[2].to_i

        result = solve l, p, c

        puts "Case ##{test_number + 1}: #{result}"
        output.puts "Case ##{test_number + 1}: #{result}"

      end
    end
  end
end

def solve l, p, c
  count = 0;
  best = l * c**(2**count)
  while best < p
    count += 1
    best = l * c**(2**count)
  end
  
  return count
end

run_tests
