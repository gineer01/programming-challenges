# This gives correct solution for small data set. It takes too long for large data set

# Date: May 23, 2010
# Time: 4:04:33 AM

def run_tests
  File.open "output_CC.txt", "w" do |output|
    File.open "C-small-practice.in" do |input|
      number_of_tests = input.gets.to_i
      number_of_tests.times do |test_number|
        test = input.gets.chomp.split /\s+/, 2
        m = test[0].to_i
        n = test[1].to_i

        board = []

        m.times do |line|
          board[line] = input.gets.chomp.to_i(16).to_s(2).rjust(n, '0')
        end

        result = solve board, m, n

        puts "Case ##{test_number + 1}: #{result}"
        p result

        output.puts "Case ##{test_number + 1}: #{result.keys.size}"
        result.keys.sort.reverse.each do |key|
          output.puts "#{key} #{result[key]}"
        end

      end
    end
  end
end

def solve board, m, n
  count = m * n
  result = {}
  while count > 0
    size = scan_board board, m, n
    if result.has_key? size
      result[size] += 1
    else
      result[size] = 1
    end

    count -= size * size
  end

  return result
end

def scan_board board, m, n
  best = 0
  best_row = 0
  best_column = 0
  m.times do |row|
    n.times do |column|
      current = find_square_on_board board, m, n, row, column
      if current > best
        best = current
        best_row = row
        best_column = column
      end
    end
  end

  best.times do |i|
    best.times do |j|
      board[best_row + i][best_column + j] = 'C'
    end
  end

  return best
end

def find_square_on_board board, m, n, row, column
  count = 1
  current_square = board[row][column]

  while ((row + count <= m) && (column + count <= n))
    count.times do |i|
      j = count - 1
      if board[row + i][column + j] == 'C'
        return count - 1
      end
      if (board[row + i][column + j] == current_square) ^ ((i+j) % 2 == 0)
        return count - 1
      end
    end

    count.times do |j|
      i = count - 1
      if board[row + i][column + j] == 'C'
        return count - 1
      end
      if ( board[row + i][column + j] == current_square) ^ ((i+j) % 2 == 0)
        return count - 1
      end
    end
    
    count += 1
  end

  return count - 1

end

run_tests