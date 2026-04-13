# CC 
PRACT 2 KVM INSTALLATION

1. sudo apt update
2. sudo apt upgrade
3.  sudo grep -c "svm\|vmx" /proc/cpuinfo
4.  sudo apt install cpu-checker
5  sudo apt install qemu-system-x86 virt-manager libvirt-daemon-system virtinst libvirt-clients bridge-utils
6  sudo systemctl enable --now libvirtd
7 sudo systemctl start libvirtd
8 sudo systemctl status libvirtd
9  Enter ctrl +c (Don't type)
10  ls /home
11  sudo adduser user_1
12  ls /home
13   sudo adduser user_1 libvirt
14    sudo adduser user_1 kvm
15   virt-manager 
if qemu-kvm not connected then perform 
perform 
16. sudo systemctl stop libvirt 
after that 
step 8 stil not connect then follow step 15 then step 8
