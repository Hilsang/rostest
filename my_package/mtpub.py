import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from datetime import datetime

class M_pub(Node):
  def __init__(self):
    super().__init__('mpub')
    self.pub = self.create_publisher(String, 'time', 10)
    self.create_timer(1, self.pubtime)
    self.count = 0
  def pubtime(self):
    time = String()
    now = datetime.now()
    time.data = now.time
    self.pub.publish(time)
    self.get_logger().info(f'Sending message : {time.data}')
    self.count += 1

def main():
  rclpy.init()
  node = M_pub()
  try:
    rclpy.spin(node)
  except:
    node.destroy_node()

if __name__ == '__main__':
  main()

