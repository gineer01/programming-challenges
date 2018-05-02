# Created by IntelliJ IDEA.
# User: dongc
# Date: Jun 25, 2010
# Time: 5:48:17 PM
# To change this template use File | Settings | File Templates.

class Graphical_Editor
  WHITE = "O"

  def create m,n
    @m = m
    @n = n
    clear
  end

  def clear
    @image = Array.new @n
    @n.times {|i| @image[i] = WHITE*@m}
  end

  def set_color x, y, color
    @image[y - 1][x - 1] = color
  end

  def save
    @image.join "\n"
  end

  def draw_vertical x, y1, y2, color
    fill_rectangle x, y1, x, y2, color
  end

  def draw_horizontal x1, x2, y, color
    fill_rectangle x1, y, x2, y, color
  end

  def fill_rectangle x1, y1, x2, y2, color
    x1, x2 = x2, x1 if x1 > x2
    y1, y2 = y2, y1 if y1 > y2
    for y in y1..y2
      for x in x1..x2
        set_color x, y, color
      end
    end
  end

  def get_color x, y
    @image[y - 1][x - 1]
  end

  def fill_region original_x, original_y, color
    stack = []

    region_color = get_color(original_x, original_y)
    if (color != region_color)
      stack.push [original_x, original_y]
    end

    while (!stack.empty?)
      current = stack.pop
      set_color *current, color
      x, y = current

      check_and_push stack, region_color, x - 1, y, color if (x - 1 > 0)
      check_and_push stack, region_color, x + 1, y, color if (x + 1 <= @m)
      check_and_push stack, region_color, x, y + 1, color if (y + 1 <= @n)
      check_and_push stack, region_color, x, y - 1, color if (y - 1 > 0)
    end    
  end

  def check_and_push stack, region_color, x, y, new_color
    color = get_color x, y
    stack.push [x, y] if (new_color != color) && (color == region_color)
  end

end

ge = Graphical_Editor.new

File.open "C:/Desktop/Temp/onlineJudge/GraphicalEditor.input" do |f|
  f.each do |line|
    param = line.split[1..-1]
    case line[0]
      when "X"
        break
      when "I"
        ge.create *param.map(&:to_i)
      when "C"
        ge.clear
      when "L"
        ge.set_color *param[0..-2].map(&:to_i), param[-1]
      when "V"
        ge.draw_vertical *param[0..-2].map(&:to_i), param[-1]
      when "H"
        ge.draw_horizontal *param[0..-2].map(&:to_i), param[-1]
      when "K"
        ge.fill_rectangle *param[0..-2].map(&:to_i), param[-1]
      when "F"
        ge.fill_region *param[0..-2].map(&:to_i), param[-1]
      when "S"
        printf("%s\n%s\n", param[0], ge.save)
      else
#        p line
    end
  end
end