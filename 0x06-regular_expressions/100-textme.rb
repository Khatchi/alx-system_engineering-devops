#!/usr/bin/env ruby

matches = ARGV[0].scan(/(\S+),(\S+),(\S+)/)
puts matches.map { |sender, receiver, flags| "#{sender},#{receiver},#{flags}" }.join("\n")

