import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String
from datetime import datetime

class M_tsub(Node):
  def __init__(self):
    super().__init__('mtsub')
    self.qos = QoSProfile(depth = 10)
    self.pub = self.create_subscription(String, 'time', self.subtime, self.qos)

  def subtime(self, time):
    self.get_logger().info(time.data)
def main():
  rclpy.init()
  node = M_tsub()
  try:
    rclpy.spin(node)
  except:
    node.destroy_node()

if __name__ == '__main__':
  main()

