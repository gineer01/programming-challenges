# Created by IntelliJ IDEA.
# User: dongc
# Date: Jun 24, 2010
# Time: 6:17:21 PM
# To change this template use File | Settings | File Templates.

SPACE = " "
VERTICAL = "|"
HORIZONTAL = "-"
BITMAP = [0077, 0024, 0155, 0165, 0126, 0163, 0173, 0025, 0177, 0167]

def get_LCD_for_digit size, digit
  bitmap = BITMAP[digit.ord - "0".ord]
  rows = []
  rows[0] = SPACE + (bitmap[0] == 1 ? HORIZONTAL : SPACE)*size + SPACE
  rows[size + 1] = SPACE + (bitmap[6] == 1 ? HORIZONTAL : SPACE)*size + SPACE
  rows[2 * size + 2] = SPACE + (bitmap[5] == 1 ? HORIZONTAL : SPACE)*size + SPACE

  rows.fill((bitmap[1] == 1 ? VERTICAL : SPACE) + SPACE*size + (bitmap[2] == 1 ? VERTICAL : SPACE), 1, size)
  rows.fill((bitmap[3] == 1 ? VERTICAL : SPACE) + SPACE*size + (bitmap[4] == 1 ? VERTICAL : SPACE), size + 2, size)

  rows
end

def get_LCD_string size, number
  matrix = number.to_s.each_char.map {|x| get_LCD_for_digit size, x}
  matrix.transpose.map(&:join).join("\n")
end

puts Time.new
File.open "UVa_706.input" do |f|
  while line = f.gets
    size, number = line.split.map(&:to_i)

    if size == 0 && number == 0
      break
    end

    printf("%s\n", get_LCD_string(size, number))
  end
end
puts Time.new