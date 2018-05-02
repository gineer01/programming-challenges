# Created by IntelliJ IDEA.
# User: dongc
# Date: May 22, 2010
# Time: 9:46:40 AM
# To change this template use File | Settings | File Templates.
def run_tests
  File.open "output_BC.txt", "w" do |output|
    File.open "C-large-practice.in" do |input|
      number_of_tests = input.gets.to_i
      number_of_tests.times do |test_number|
        n = input.gets.to_i

        p n

        result = solve n
        
        p result
        output.puts "Case ##{test_number + 1}: #{result}"

      end
    end
  end
end

C=[]
C[0] = [1]

for i in 1..500
  C[i] =[]
  C[i][0] = C[i][i] = 1
  for j in 1..(i-1)
    C[i][j] = (C[i-1][j-1] + C[i-1][j]) % 100003
  end
end

def n_choose_k n, k
  if k == 0
    return 1
  end

  if k > n
    return 0
  end

  return C[n][k]
end

A = []
A[0] = [0]
def solve n
  if (n == 0)
    return 0
  end

  if !A[n].nil?
    return sum_row n
  end

  n.times do |i|
    if A[i] == nil
      puts "Solving for #{i}"
      solve i
    end
  end

  A[n] = []
  A[n][1] = 1
  A[n][n-1] = 1
  for i in 2..(n-2)
    A[n][i] = calculate n, i
  end

  return sum_row n
end

def sum_row n
  result = 0
  for i in 1..(n-1)
    result += A[n][i]
  end
  return (result % 100003)
end

def calculate n,length
  result = 0;

  for sub_length in 1..(length - 1)
    k = length - sub_length - 1;
    choice = n - length - 1;
    result += A[length][sub_length] * n_choose_k(choice, k)
  end

  return result % 100003;
end

run_tests