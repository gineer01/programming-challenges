#Code golf challenge: http://stackoverflow.com/questions/2985540/code-golf-banner-generation
# The shortest source code to generate banner. Input should contain only [A-Z! ]
# Example: input: THANKS!
# Output:
#"TTT H H  A  NNN K K  SS !!! \n"
#" T  H H A A N N K K S   !!! \n"
#" T  HHH AAA N N KK   S  !!! \n"
#" T  H H A A N N K K   S     \n"
#" T  H H A A N N K K SS  !!! \n"

i=gets;5.times{|t|p i.gsub(/./){|c|j=3*(c>?@?c.ord-64:0);(3*t..3*t+2).map{|d|"mini5mbmzjf2bqjmof3prl72i5pn138iuhylmkpi65i278kq3qjfaihyjb66787odp8ktiy5hwt78tmnb"[j..j+2].to_i(36)[d]==1?c:" "}*""+" "}}