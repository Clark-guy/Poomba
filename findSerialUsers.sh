ls -l /dev/serial0 /dev/ttyAMA0 /dev/ttyS0
ps aux | grep -E 'serial|getty|ttyAMA|ttyS0'
sudo systemctl status serial-getty@ttyAMA0.service serial-getty@ttyS0.service
