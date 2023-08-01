#!/usr/bin/env ruby

matches = ARGV[0].scan(/hbt{2,5}n/)
puts matches.join
