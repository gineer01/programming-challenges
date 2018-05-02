# Created by IntelliJ IDEA.
# User: dongc
# Date: Jun 26, 2010
# Time: 1:13:59 AM
# To change this template use File | Settings | File Templates.

class Simulator
  MODULO = 1000

  def initialize
    @ram = Array.new 1000, 0
    @reg = Array.new 10, 0
    @ip = 0
    @count = 0
  end

  def execute ram_content
    @ram[0...ram_content.length] = ram_content

    loop {break if execute_instruction}

    @count
  end

  def execute_instruction
    @count += 1
    instruction = @ram[@ip]
    code, a, b = instruction/100, (instruction/10)%10, instruction % 10

    case code
      when 1
        return true;
      when 2
        @reg[a] = b
        @ip += 1
      when 3
        @reg[a] = (@reg[a] + b) % MODULO
        @ip += 1
      when 4
        @reg[a] = (@reg[a] * b) % MODULO
        @ip += 1
      when 5
        @reg[a] = @reg[b]
        @ip += 1
      when 6
        @reg[a] = (@reg[a] + @reg[b]) % MODULO
        @ip += 1
      when 7
        @reg[a] = (@reg[a] * @reg[b]) % MODULO
        @ip += 1
      when 8
        @reg[a] = @ram[@reg[b]]
        @ip += 1
      when 9
        @ram[@reg[b]] = @reg[a]
        @ip += 1
      when 0
        if @reg[b] == 0
          @ip += 1
        else
          @ip = @reg[a]
        end
    end

    false
  end

end

File.open 'C:\Desktop\Temp\onlineJudge\Simulator.input' do |f|
  n = f.gets.to_i
  f.gets
  n.times do
    input = []
    while (line = f.gets) && line.strip.length > 0
      input << line.strip.to_i
    end

    sim = Simulator.new
    puts sim.execute(input)
  end
end