import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String

class Mt_sub(Node):
  def __init__(self):
    super().__init__('msub')
    self.qos = QoSProfile(depth = 10)
    self.pub = self.create_subscription(String, 'time', self.messagesub, self.qos)

  def messagesub(self, msg):
    self.get_logger().info(msg.data)
def main():
  rclpy.init()
  node = Mt_sub()
  try:
    rclpy.spin(node)
  except:
    node.destroy_node()

if __name__ == '__main__':
  main()

