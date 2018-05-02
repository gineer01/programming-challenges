#Code golf challenge: http://stackoverflow.com/questions/3324301/code-golf-digital-clock
# Write the smallest possible program (least number of characters) that takes input
# in the hh:mm format and outputs this as a digital clock (seven-segment display).

puts gets.chomp.each_char.map{|b|[[7,0,7],[1,3,2],[4,6,5]].map{|p|p.map{|i|"w$]m.k{%\x7Fo?zS|[\e"[b.to_i 16].ord[i]>0?i%3>0?"|":"_":" "}.join}}.transpose.map(&:join).join"\n"