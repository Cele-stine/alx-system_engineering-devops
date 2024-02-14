file { '/root/.ssh/config':
  ensure  => 'present'
  content => template('0x0B-ssh/ssh_client_config.erb')
  owner   => 'root'
  mode    => '0600'
}
