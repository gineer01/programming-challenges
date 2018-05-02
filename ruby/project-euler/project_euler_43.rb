a = %w[ 0 1 2 3 4 5 6 7 8 9 ]

def pick_digit a, pos, string
  if pos == 10
    puts string
  end

  for digit in a
    temp = string + digit
    case pos
      when 5
        next if digit.to_i % 5 != 0
      when 3
        next if digit.to_i.odd?
      when 4
        next if temp[2..4].to_i % 3 != 0
      when 6
        next if temp[4..6].to_i % 7 != 0
      when 7
        next if temp[5..7].to_i % 11 != 0
      when 8
        next if temp[6..8].to_i % 13 != 0
      when 9
        next if temp[7..9].to_i % 17 != 0
    end

    pick_digit a - [digit], pos + 1, temp
  end
end

def solution?(num_s)
  %w(2 3 5 7 11 13 17).each.with_index {|n, i| return false unless num_s[i + 1..i + 3].to_i % n.to_i == 0 }
end

def another_solution
  %w[ 0 1 2 3 4 5 6 7 8 9 ].permutation.map(&:join).select{|i| solution? i}.map(&:to_i).inject(&:+)
end
puts Time.new
#pick_digit a, 0, ""
puts another_solution
#puts solution? '1406357289'
puts Time.new