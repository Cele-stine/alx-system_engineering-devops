# A file that kills a process.

exec { 'kill' :
  command     => '/usr/bin/pkill killmenow',
  refreshonly => true,
  onlyif      => '/usr/bin/pgrep -f killmenow',
}
