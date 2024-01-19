# install_flask.pp

# Install python3-pip
package { 'python3-pip':
  ensure => 'latest',
}

# Install Flask using pip3
package { 'Flask':
  ensure   => '2.1.0',  # Set the desired version of Flask
  provider => 'pip3',
}
