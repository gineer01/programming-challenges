# Created by IntelliJ IDEA.
# User: dongc
# Date: May 23, 2010
# Time: 2:26:28 AM
# To change this template use File | Settings | File Templates
class Line
  attr :a, :b

  def initialize a, b
    @a = a
    @b = b
  end

  def intersect? line
    (@a > line.a) ^ (@b > line.b)
  end
end

def run_tests
  File.open "output_CA.txt", "w" do |output|
    File.open "A-large-practice.in" do |input|
      number_of_tests = input.gets.to_i
      number_of_tests.times do |test_number|
        n = input.gets.to_i

        wire = []
        count = 0
        n.times do
          coord = input.gets.chomp.split /\s+/, 2
          line_new = Line.new(coord[0].to_i, coord[1].to_i)
          wire.each do |other_line|
            if line_new.intersect? other_line
              count += 1
            end
          end
          wire<< line_new
        end
        
        puts "Case ##{test_number + 1}: #{count}"
        output.puts "Case ##{test_number + 1}: #{count}"

      end
    end
  end
end

run_tests

