# Created by IntelliJ IDEA.
# User: dongc
# Date: May 17, 2010
# Time: 2:32:40 PM
# To change this template use File | Settings | File Templates.

File.open "output.txt", "w" do |output|
  File.open "file.txt" do |input|
    number_of_tests = input.gets.to_i
    number_of_tests.times do |test_number|
      test = input.gets.split /\s+/, 2
      n = test[0].to_i
      k = test[1].to_i

      on = true
      n.times do |i|
        if k[i] == 0
          on = false
          break
        end
      end

      output.puts "Case ##{test_number + 1}: " + (on ? "ON":"OFF")

    end
  end
end

