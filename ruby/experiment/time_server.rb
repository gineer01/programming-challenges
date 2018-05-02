require 'gserver'

# A server that returns the time in seconds since 1970.
# and ask for your name and say hello
class TimeServer < GServer
  def initialize(port=10001, * args)
    super(port, * args)
  end

  def serve(io)
    io.puts(Time.now.to_i)
    io.puts "What is your name?\r\n"
    line = io.gets
    io.puts "Hello #{line}"
  end
end

# Run the server with logging enabled (it's a separate thread).
server = TimeServer.new
server.audit = true # Turn logging on.
server.start.join
