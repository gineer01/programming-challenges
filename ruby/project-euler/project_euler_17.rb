# Created by IntelliJ IDEA.
# User: dongc
# Date: May 24, 2010
# Time: 6:51:26 PM
# To change this template use File | Settings | File Templates.
def speak_number n
  first_ten = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
  tens = ["zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

  if n == 1000
    return "one thousand"
  end

  if n == 0
    return "zero"
  end

  result = ""

  hundred = n / 100
  remaining = n % 100

  if (hundred > 0)
    result += first_ten[hundred] + " hundred"
    if (remaining > 0)
      result += " and "
    end
  end

  if (remaining >= 20)
    result += tens[remaining/10] + " " + first_ten[remaining%10]
  else
    result += first_ten[remaining]
  end

  return result

end

puts speak_number(342).gsub(/\s+/,"").length
puts speak_number(115).gsub(/\s+/,"").length

count = 0
for i in 1..1000
  count += speak_number(i).gsub(/\s+/,"").length
end

p count