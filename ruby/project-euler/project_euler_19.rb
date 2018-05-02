# Created by IntelliJ IDEA.
# User: dongc
# Date: May 24, 2010
# Time: 7:24:38 PM
# To change this template use File | Settings | File Templates.
require "Date"

def print_sundays(d1, d2)
  count = 0
  d1 +=1 while (d1.wday != 0)
  d1.step(d2, 7) do |date|
#    puts "#{Date::MONTHNAMES[date.mon]} #{date.day}"
    if date.day == 1
      count += 1
    end
  end
  return count
end

p print_sundays(Date::civil(1901, 1, 1), Date::civil(2000, 12, 31))