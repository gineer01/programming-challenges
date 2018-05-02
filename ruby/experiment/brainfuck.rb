# Created by IntelliJ IDEA.
# User: dongc
# Date: May 17, 2010
# Time: 4:42:41 PM
# To change this template use File | Settings | File Templates.



class Intepreter
  def initialize
    @data = []
    @data_pointer = 0
    @program_pointer = 0
  end

  def intepret_script script
    @program = script
    while @program_pointer < @program.length
#      puts @program[@program_pointer, 1]
      case @program[@program_pointer]
        when ?> then
          @data_pointer += 1

        when ?< then
          @data_pointer -= 1

        when ?+ then
          data =  @data[@data_pointer] ? @data[@data_pointer] : 0
          @data[@data_pointer] = (data + 1)

        when ?- then
          data =  @data[@data_pointer] ? @data[@data_pointer] : 0
          @data[@data_pointer] = data - 1

        when ?. then
          print @data[@data_pointer].chr

        when ?, then
          @data[@data_pointer] = gets[0]

        when ?[ then
          if @data[@data_pointer] == 0
            count = 1
            while count > 0
              @program_pointer = @program_pointer + 1
              if @program[@program_pointer] == ?[
                count += 1
              elsif @program[@program_pointer] == ?]
                count -= 1
              end
            end
          end

        when ?] then
          if @data[@data_pointer] != 0
            count = 1
            while count > 0
              @program_pointer -= 1
              if @program[@program_pointer] == ?]
                count += 1
              elsif @program[@program_pointer] == ?[
                count -= 1
              end
            end
          end

      end
      @program_pointer += 1
    end
  end
end

script = File.read "script.txt"
#p script
interpreter = Intepreter.new
interpreter.intepret_script(script)
#interpreter.intepret_script ",[.,]"
