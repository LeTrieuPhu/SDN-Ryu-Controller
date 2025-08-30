# Triển khai mạng SDN với Controller Ryu
## Cài đặt
1. Cài đặt mininet
   - Tải và cài đặt ubuntu 20.04: https://releases.ubuntu.com/focal/ubuntu-20.04.6-desktop-amd64.iso
   - Sau khi cài đặt ubuntu, tải mininet: sudo apt install mininet
   - Kiểm tra đã tải thành công chưa: mn --version
2. Cài đặt Ryu:
   - Cài đặt python và pip: sudo apt-get install python3-pip python3 python2
   - Cài đặt Ryu: sudo pip3 install ryu
   - Tải lại eventlet: pip3 install eventlet==0.30.2
   - Kiểm Tra: ryu-manager --version
  
## Hướng dẫn sử dụng
1. Clone dự án : **git clone https://github.com/LeTrieuPhu/SDN-Ryu-Controller.git**
2. Khởi động Ryu Controller: **sudo ryu-manager simple_switch_13_custom.py rest_router_FW_custom.py /home/mininet/Desktop/DoAn_QTM/flowmanager/flowmanager.py --observe-links --ofp-tcp-listen-port 6633 --wsapi-port 8085**
    -  **simple_switch_13_custom.py:** File cấu hình switch.
    -  **rest_router_FW_custom.py:** File cấu hình router.
    -  **/home/mininet/Desktop/DoAn_QTM/flowmanager/flowmanager.py:** Đường dẫn giao diện web flowmanager.
    -  **--observe-links:** Khi bật tính năng này, Ryu Controller sẽ theo dõi trạng thái của các liên kết giữa các switch OpenFlow và tự động cập nhật khi có thay đổi về cấu trúc mạng.
    -  **--ofp-tcp-listen-port 6633:** Tham số dùng để chỉ định cổng TCP mà Ryu Controller sẽ lắng nghe các kết nối từ các switch OpenFlow.
    -  **--wsapi-port 8085:** Cung cấp WebSocket API qua cổng 8085 để kết nối từ các ứng dụng Flowmanager
3. Khởi động mạng mininet: **sudo python2 topoX.py**
4. Cấu hình router qua API:
    - **curl -X POST -d '{"address": "10.0.10.1/24"}' http://localhost:8085/router/0000000000000021**
    - **curl -X POST -d '{"address": "10.0.20.1/24"}' http://localhost:8085/router/0000000000000021**
    - **address:** Địa chỉ IP gateway của 2 lớp mạng 
    - **0000000000000021:** Địa chỉ MAC của router được cấu hình trong topo
5. Truy cập giao diện Web: http://localhost:8085/home/flows.html

## Demo
1. Topo
   - Topo 1: Sử dụng 2 Switch, 1 router và 4 host. Mỗi lớp mạng kết nối với 1 Switch
![Topo 1](https://github.com/LeTrieuPhu/SDN-Ryu-Controller/blob/main/picture/Topo1.png)
   - Topo 2: Sử dụng 2 Switch, 1 router và 7 host. Mỗi lớp mạng kết nối với 1 Switch, có tích hợp firewall không cho lớp mạng 100.0.0.0/8 ping qua lớp mạng 10.0.0.0/24
![Topo 2](https://github.com/LeTrieuPhu/SDN-Ryu-Controller/blob/main/picture/Topo2.png)
   - Topo 3: Sử dụng 2 Router và 4 host. Hai host khác lớp mạng kết nối với một router
![Topo 3](https://github.com/LeTrieuPhu/SDN-Ryu-Controller/blob/main/picture/Topo3.png)
## link video demo
https://drive.google.com/file/d/1hCcG5Fd1-RQPaLl8S83lTr9xTTZm-i9P/view?usp=drive_link
