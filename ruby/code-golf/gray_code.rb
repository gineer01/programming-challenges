#Gray code generator

def g n
  if n == 1
    yield "0"
    yield "1"
  else
    a = []
    g(n - 1) {|x| a.push x; yield "0"+x}
    a.size.times {x = a.pop; yield "1"+x}
  end
end

g(4) {|x| puts x}