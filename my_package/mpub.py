import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class M_pub(Node):
  def __init__(self):
    super().__init__('mpub')
    self.pub = self.create_publisher(String, 'messagepub', 10)

def main():
  rclpy.init()
  node = M_pub()
  msg = String()
  msg.data = 'hello world'
  while True:
    node.pub.publish(msg)
  node.destroy_node()

if __name__ == '__main__':
  main()

