# This is a manifest to install flask version 2.1.0 .
$version = '2.1.0'
package { 'flask' :
  ensure   => $version,
  provider => 'pip3',
}
