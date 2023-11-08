# Use the file_edit resource type to edit a specific file
exec { 'fix_line':
  command     => "/bin/sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  provider => 'windows terminal'
}

