# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "trusty64"
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"
  config.vm.network :forwarded_port, guest: 80, host: 8028, auto_correct:
true
  config.vm.synced_folder "scripts", "/home/vagrant/scripts",
    owner: "vagrant",
    group: "root",
    mount_options: ["dmode=1710"] 
 config.vm.synced_folder "challenges", "/home/vagrant/challenges"
 config.vm.provision :shell, :path => "scripts/web_setup.sh"
  config.ssh.forward_agent = true

  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--memory", "8192"]
  end
end
