# Created by IntelliJ IDEA.
# User: dongc
# Date: Jun 18, 2010
# Time: 2:19:16 PM
# To change this template use File | Settings | File Templates.

$cache = {1 => 1}

#With cache, taking about 3 s
def get_cycle_with_cache x
  case
    when $cache.has_key?(x)
      $cache[x]
    when x[0] == 0 #even
      $cache[x] = 1 + get_cycle_with_cache(x/2)
    when x[0] == 1 #odd
      $cache[x] = 2 + get_cycle_with_cache((3*x + 1)/2)
  end
end

#Without cache, taking about 20 s
def get_cycle x
  count = 0
  while (x > 1)
    case
      when x[0] == 0 #even
        count += 1
        x = x/2
      when x[0] == 1 #odd
        count += 2
        x = ((3*x + 1)/2)
    end
  end
  count += 1
end

def solve i, j
  i, j = j, i if i > j
  i.upto(j).map {|x| get_cycle_with_cache x}.max
end

puts Time.new
File.open "online_judge_100.input" do |f|
  f.each do |line|
    i, j = line.split.map{|x| x.to_i}
    printf "%d %d %d\n", i, j, solve(i, j)
  end
end
puts Time.new