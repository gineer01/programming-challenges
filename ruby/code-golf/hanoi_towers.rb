#Output an ASCII animation of moving disks between the rods for Tower of Hanoi problem 

class Hanoi_tower
  def initialize n, a, b, c
    @n = n
    @columns = {a => (1..n).to_a.reverse, b => [], c => []}
  end

  def move from, to
    disc = @columns[from].pop
    @columns[to].push disc
  end

  def to_s
    output = ""
    @columns.each do |key, value|
      output << ("%s : %s \n" % [key, value.to_s])
    end
    output
  end

  def display
    @columns.map { |key, value| display_column key, value }.transpose.map(& :join).join "\n"
  end

  def display_column key, value
    width = 2*@n
    (0...@n).map { |i|
      i >= value.length ? "||".center(width) : ("#"*2*value[i]).center(width)
    }.reverse << "="*width << key.to_s.center(width) 
  end

  def Hanoi_tower.solve n, from, to, extra, & block
    if n == 1
      yield from, to
    else
      solve n-1, from, extra, to, & block
      yield from, to
      solve n-1, extra, to, from, & block
    end
  end
end


number_of_discs = 5
tower = Hanoi_tower.new number_of_discs, :a, :b, :c

puts tower.display

Hanoi_tower.solve(number_of_discs, :a, :b, :c) { |from, to|
  tower.move from, to
  puts tower.display
  sleep 0.1
}

