# rostest

this tis first edit



- - -

## 2023_02_13

- - -

* first
  * turtlebot3
  * VMware 17 Ubuntu 20.04
* second
  * ROS2 DDS explain
* third

```shell
ros2 topic pub --rate 1 /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"
// 원 그리기
ros2 service call /spawn turtlesim/srv/Spawn "{x: 2, y: 2, theta: 0.2, name: 'turtle2'}"
// 스폰
ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute "{theta: -3}"
// 회전
ros2 param load /turtlesim ./turtlesim.yaml
// 파라미터 불러오기
ros2 param get /turtlesim background_r
// 파라미터 값 보기
ros2 param set /turtlesim background_b 100
// 파라미터 값 변경
