#---
# Excerpted from "Programming Ruby",
# published by The Pragmatic Bookshelf.
# Copyrights apply to this code. It may not be used to create training material,
# courses, books, articles, and the like. Contact us if you are in doubt.
# We make no guarantees that this code is fit for any purpose.
# Visit http://www.pragmaticprogrammer.com/titles/ruby3 for more book information.
#---
triangular_numbers = Enumerator.new do |yielder|
  number = 0
  count = 1
  loop do
    number += count
    count += 1
    yielder.yield number
  end
end

5.times { puts triangular_numbers.next }

#---
# Excerpted from "Programming Ruby",
# published by The Pragmatic Bookshelf.
# Copyrights apply to this code. It may not be used to create training material,
# courses, books, articles, and the like. Contact us if you are in doubt.
# We make no guarantees that this code is fit for any purpose.
# Visit http://www.pragmaticprogrammer.com/titles/ruby3 for more book information.
#---
natural_numbers = Enumerator.new do |yielder|
  number = 2
  loop do
    yielder.yield number
    number += 1
  end
end

class Enumerator
  def lazy_select(& block)
    Enumerator.new do |yielder|
      self.each do |val|
        yielder.yield(val) if block.call(val)
      end
    end
  end

  def lazy_map(& block)
    Enumerator.new do |yielder|
      self.each do |value|
        yielder.yield(block.call(value))
      end
    end
  end
end

def sieve enum, limit
  Enumerator.new do |yielder|
    loop do
      first = enum.next
      if (first < limit)
        enum = enum.lazy_select { |x| x % first != 0 }
      end
      yielder.yield first
    end
  end
end
require 'prime'

puts Time.new
p (sieve natural_numbers, 110).first(10000)
puts Time.new
p natural_numbers.lazy_select{|x| x.prime?}.first(10000)
puts Time.new
