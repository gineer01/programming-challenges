# Created by IntelliJ IDEA.
# User: dongc
# Date: May 25, 2010
# Time: 6:25:15 PM
# To change this template use File | Settings | File Templates.

class Digit
  def initialize
    @current = 1
    @digit_count = 0
  end

  def get_digit i
    if i < @digit_count
      raise "Cannot go backward"
    end

    while (@digit_count + @current.to_s.length) < i
      @digit_count += @current.to_s.length
      @current += 1
    end

    current_string = @current.to_s
    return current_string[i - @digit_count - 1,1]
    
  end
end

digit = Digit.new

result = 1
for i in 0..6
  puts "#{10**i}"
  puts result *= digit.get_digit(10**i).to_i
end

p result

