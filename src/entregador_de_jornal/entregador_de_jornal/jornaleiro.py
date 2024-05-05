import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist 
from turtlesim.srv import Spawn, Kill, SetPen
import time

class GarbelitoJornaleiro(Node):
    def __init__(self):
        super().__init__('garbelito_jornaleiro')
        self.jornaleiro = self.create_publisher(
            msg_type=Twist,
            topic='/garbelito_bananildo/cmd_vel',  # Assuming the turtle is named "garbelito_bananildo"
            qos_profile=10
        )

        # Call the spawn_turtle method to create the turtle
        self.spawn_turtle()

        timer_period = 0.5
        self.timer = self.create_timer(
                timer_period,
                self.timer_callback
            )

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 10.0  # Reduce linear velocity
        msg.angular.z = 10.0  # Reduce angular velocity
        self.jornaleiro.publish(msg=msg)
        self.get_logger().info("Olha o jornallllll Garbelitooooooooo !!!!!!!!!")

    def move_turtle(self, distance, angle):
        msg = Twist()
        msg.linear.x = distance
        msg.angular.z = angle
        self.jornaleiro.publish(msg)
        time.sleep(1)  # Adjust sleep time based on the speed of the turtle

    def spawn_turtle(self):
        spawn_client = self.create_client(Spawn, '/spawn')
        while not spawn_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn('Waiting for /spawn service...')
        request = Spawn.Request()
        request.name = 'garbelito_bananildo'
        request.x = 5.0
        request.y = 5.0
        request.theta = 0.0
        future = spawn_client.call_async(request)

        # Block until service call is completed
        rclpy.spin_until_future_complete(self, future)

        if future.result() is not None:
            self.get_logger().info('Spawned a turtle named "garbelito_bananildo"')
            self.set_pen()
        else:
            self.get_logger().error('Failed to spawn turtle')

        # Call the kill_turtle method after 4 seconds
        self.kill_turtle()

    def reset(self):
        self.create_client()

    def kill_turtle(self):  
        time.sleep(4)
        kill_client = self.create_client(Kill, '/kill')
        while not kill_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn('Waiting for /kill service...')
        kill_request = Kill.Request()
        kill_request.name = 'turtle1'
        kill_future = kill_client.call_async(kill_request)

        # Block until service call is completed
        rclpy.spin_until_future_complete(self, kill_future)

        if kill_future.result() is not None:
            self.get_logger().info('Killed the turtle named "Turtle1"')
        else:
            self.get_logger().error('Failed to kill turtle')

    def set_pen(self):
        set_pen_client = self.create_client(SetPen, '/garbelito_bananildo/set_pen')
        while not set_pen_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn('Waiting for /garbelito_bananildo/set_pen service...')
        set_pen_request = SetPen.Request()
        set_pen_request.width = 4
        set_pen_request.r = 255
        set_pen_request.g = 0
        set_pen_request.b = 0

        # Call the service to set the pen properties
        future = set_pen_client.call_async(set_pen_request)
        rclpy.spin_until_future_complete(self, future)
        if future.result() is not None:
            self.get_logger().info('Set pen properties for "garbelito_bananildo"')
        else:
            self.get_logger().error('Failed to set pen properties')

def desenha(args=None):
    rclpy.init(args=args)

    jornaleiro = GarbelitoJornaleiro()

    rclpy.spin(jornaleiro)

    jornaleiro.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    desenha()
