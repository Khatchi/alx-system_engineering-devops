#!/usr/bin/env ruby

log_content = File.read(ARGV[0])
matches = log_content.scan(/(\S+),(\S+),(\S+)/)
puts matches.map { |sender, receiver, flags| "#{sender},#{receiver},#{flags}" }.join("\n")

