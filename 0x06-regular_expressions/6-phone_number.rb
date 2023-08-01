#!/usr/bin/env ruby

matches = ARGV[0].scan(/\A\d{10}\z/)
puts matches.join
