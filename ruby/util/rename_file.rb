dir_path = "./images"
WIDTH = 9

Dir.foreach(dir_path) do |file_name|
  file_path = dir_path + File::SEPARATOR + file_name
  if File.file?(file_path)
    if (file_name =~ /(\d+)\.(\d+)\.(.*)/)   #using regex to parse the name
      data =  Regexp.last_match              #getting the group

      #the new name : first digit group . zero-padded second group . third group
      new_name = "#{data[1]}.#{data[2].rjust(WIDTH, '0')}.#{data[3]}"
      new_path = dir_path + File::SEPARATOR + new_name
      
      puts "Changing #{file_path} to #{new_path}"
      File.rename(file_path, new_path)
    else
      puts "#{file_path} doesn't match pattern. Check your regex"
    end
  end
end