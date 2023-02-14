import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile

class M_turtle(Node):
  def __init__(self):
    super().__init__('move turtle')
    self.qos = QoSProfile(depth = 10)
    self.pub = self.create_publisher(Twist, 'turtle/cmd_vel', 10)
    self.create_timer(1, self.pubmessage)
    self.count = 0
  def pubmessage(self):
    msg = Twist()
    msg.linear.x = 1.5
    msg.linear.y = 0.0
    msg.linear.z = 0.0
    msg.angular.x = 0.0
    msg.angular.y = 0.0
    msg.angular.z = 0.5
    self.pub.publish(msg)
    self.get_logger().info(f'Sending message : {msg}')
    self.count += 1

def main():
  rclpy.init()
  node = M_turtle()
  try:
    rclpy.spin(node)
  except:
    node.destroy_node()

if __name__ == '__main__':
  main()

