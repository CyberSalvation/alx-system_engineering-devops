# Ensure the apache2 service is running and enabled
service { 'apache2':
  ensure => 'running',
  enable => true,
}

