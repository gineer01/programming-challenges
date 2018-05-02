# Created by IntelliJ IDEA.
# User: dongc
# Date: May 21, 2010
# Time: 6:09:46 PM
# To change this template use File | Settings | File Templates.

def run_tests
  File.open "output_1_big.txt", "w" do |output|
    File.open "A-large.in" do |input|
      number_of_tests = input.gets.to_i
      number_of_tests.times do |test_number|
        test = input.gets.split /\s+/, 2
        n = test[0].to_i
        k = test[1].to_i
        table=[]
        n.times do |row|
          table[row] = input.gets.chomp
        end

        p table
        table = rotate_table table, n
        p table
        puts check_k_in_table table, n, k
        output.puts "Case ##{test_number + 1}: " + check_k_in_table(table, n, k)

      end
    end
  end
end


def check_row table, n, k, x, y
  if ((y + k) > n)
    return false;
  end

  value = table[x][y]

  k.times do |i|
    if table[x][y + i] != value
      return false
    end
  end

  return true
end

def check_column table, n, k, x, y
  if ((x + k) > n)
    return false;
  end

  value = table[x][y]

  k.times do |i|
    if table[x + i][y] != value
      return false
    end
  end

  return true
end

def check_backlash table, n, k, x, y
  if ((x + k) > n) || ((y + k) > n)
    return false;
  end

  value = table[x][y]

  k.times do |i|
    if table[x + i][y + i] != value
      return false
    end
  end

  return true
end

def check_lash table, n, k, x, y
  if ((k - y) > 1) || ((x + k) > n)
    return false;
  end

  value = table[x][y]

  k.times do |i|
    if table[x + i][y - i] != value
      return false
    end
  end

  return true
end

def check_position table, n, k, x, y
  value = table[x][y]
  if value == '.'
    return false
  end

  if check_column table, n, k, x, y
    return true
  end
  if check_row  table, n, k, x, y
    return true
  end
  if check_backlash table, n, k, x, y
    return true
  end
  if check_lash table, n, k, x, y
    return true
  end

  return false
end

def check_k_in_table table, n, k
  result = ""
  for row in 0..(n -1)
    for column in 0..(n-1)
      if check_position table, n, k, row, column
        if (result == "")
          result = table[row][column]
        elsif (result != table[row][column])
          return "Both";
        end
      end
    end
  end
  if (result == "")
    return 'Neither'
  else
    return result == "R" ? "Red" : "Blue"
  end
end

def rotate_table table, n
  new_table = []
  table.length.times do |i|
    row = table[i]
    new_table[i] = row.gsub(/\.+($|(?=R|B))/, "").rjust(n, '.')
  end
  return new_table
end

run_tests