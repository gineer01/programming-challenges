# Created by IntelliJ IDEA.
# User: dongc
# Date: Jun 20, 2010
# Time: 12:52:33 AM
# To change this template use File | Settings | File Templates.

MINE = "*"
def count field, n, m, x, y
  result = 0
  for i in x-1..x+1
    next if i < 0 || i >= n
    for j in y-1..y+1
      case
        when (j < 0), (j >= m), (i == x) && (j == y)
          next
        else
          result += 1 if field[i][j] == MINE
      end
    end
  end
  result
end

def solve field, n, m
  field.map.with_index do |row, row_index|
    row.each_char.map.with_index do |char, column_index|
      if char == MINE
        MINE
      else
        count(field, n, m, row_index, column_index).to_s
      end
    end.join
  end.join "\n"
end

def format_output index, string
  "Field #%d:\n%s" % [index, string]
end

puts Time.new
output = []
File.open "UVa_10189.input" do |f|
  index = 0
  while line = f.gets
    n, m = line.split.map{|x| x.to_i}

    if n == 0 && m == 0
      break
    end

    field = []
    n.times do
      field << f.gets.chomp
    end

    index += 1
    output << format_output(index, solve(field, n, m))
  end
end

print output.join "\n\n"

puts Time.new

