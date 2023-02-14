import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class M_pub(Node):
  def __init__(self):
    super().__init__('mpub')
    self.pub = self.create_publisher(String, 'messagepub', 10)
    self.create_timer(1, self.pubmessage)

    def pubmessage(self):
      msg = String()
      msg.data = 'hello world'
      self.pub.publish(msg)

def main():
  rclpy.init()
  node = M_pub()
  try:
    rclpy.spin()
  except:
    node.destroy_node()

if __name__ == '__main__':
  main()

