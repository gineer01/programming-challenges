# Created by IntelliJ IDEA.
# User: dongc
# Date: May 21, 2010
# Time: 7:40:20 PM
# To change this template use File | Settings | File Templates.

def run_tests
  File.open "output_B.txt", "w" do |output|
    File.open "A-large.in" do |input|
      number_of_tests = input.gets.to_i
      number_of_tests.times do |test_number|
        n_and_m = input.gets.split /\s+/, 2
        n = n_and_m[0].to_i
        m = n_and_m[1].to_i

        current = []
        n.times do |i|
          current[i] = input.gets.chomp
        end

        to_create = []
        m.times do |i|
          to_create[i] = input.gets.chomp
        end

        p current
        p to_create
        count = solve current, to_create
        p count
        output.puts "Case ##{test_number + 1}: #{count}"

      end
    end
  end
end

class MyDirectory
  def initialize name
    @name = name
    @children = {}
  end

  def mk_single_dir name
    if @children.has_key? name
      return false
    else
      @children[name] = MyDirectory.new name
    end
  end

  def mk_dir relative_path
    if relative_path.nil?
      return 0
    end

    directories = relative_path.split "/", 2
    first = directories[0];
    next_directories = directories[1];

    count = 0;
    if (@children.has_key? first)
      count += @children[first].mk_dir next_directories
    else
      new_dir = mk_single_dir first
      count += 1
      count += new_dir.mk_dir next_directories
    end

    return count
  end
end

def solve current, to_create
  root = MyDirectory.new "/"
  current.each do |path|
    root.mk_dir path[1..-1]
  end

  count = 0
  to_create.each do |path|
    count += root.mk_dir path[1..-1]
  end

  return count
end

run_tests