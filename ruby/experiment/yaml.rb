# Created by IntelliJ IDEA.
# User: dongc
# Date: May 16, 2010
# Time: 6:30:48 PM
# To change this template use File | Settings | File Templates.
require 'yaml'

#test_array=['Give quiche a chane', "fadf", "fadfadfs"]
#test_string = test_array.to_yaml
filename = "file.txt"
#File.open filename, 'w' do |f|
#  f.write test_string
#end

read_string = File.read filename
read_array = YAML::load read_string

puts read_array
puts read_array.type