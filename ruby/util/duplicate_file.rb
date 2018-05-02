# Created by IntelliJ IDEA.
# User: dongc
# Date: May 18, 2010
# Time: 6:48:07 PM
# To change this template use File | Settings | File Templates.

require 'find'
require 'digest/md5'

sizeHash = {}

File.open "z_backup.txt", "w" do |f|
  Find.find("Z:/") do |path|
    if (!FileTest.directory?(path) && File.readable?(path))
      begin
        hash = Digest::MD5.hexdigest(File.read(path))
        hash = File.size path
        if sizeHash.key? hash
          f.write path + " and " + sizeHash[hash] + " are duplicate\n" if (Digest::MD5.hexdigest(File.read(path)) == Digest::MD5.hexdigest(File.read(sizeHash[hash])))
        else
          sizeHash[hash] = path
        end
      rescue
        $stderr.print "#{path} cannot be read\n"
      end
    end
    f.puts path
  end
end