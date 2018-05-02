#Convert decimal numbers to Roman numeral

# Date: May 16, 2010
# Time: 5:28:56 PM


def roman_numeral value
  if (value > 3000) || (value <= 0)
    return nil
  end

  partial_string = process(value, 1000, 'M', nil, nil)
  value %= 1000
  partial_string += process(value, 100, 'C', 'D', 'M')
  value %= 100
  partial_string += process(value, 10, 'X', 'L', 'C')
  value %= 10
  partial_string += process(value, 1, 'I', 'V', 'X')
  partial_string
end

def process value, base, base_symbol, fifth_symbol, next_symbol
  multiple = value / base
  case (multiple)
    when 1..3
       base_symbol*multiple
    when 4
       base_symbol + fifth_symbol
    when 5..8
       fifth_symbol + base_symbol*(multiple - 5)
    when 9
       base_symbol + next_symbol
    else
      ""
  end
end

puts roman_numeral(1909)
puts roman_numeral(1808)