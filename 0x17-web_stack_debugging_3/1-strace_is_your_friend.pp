# Use the file_edit resource type to edit a specific file
file_line { 'fix_error':
    path    => '/var/www/html/wp-settings.php',
    line => 'php',
    match  => 'phpp',
}

