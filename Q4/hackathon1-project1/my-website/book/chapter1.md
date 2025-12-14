---
title: Chapter 1 - ROS 2 Architecture Deep Dive
---

# Chapter 1: ROS 2 Architecture Deep Dive

In the previous module, we introduced the concept of ROS 2 as the "nervous system" of robots. Now, let's explore the architecture in greater depth to truly understand how ROS 2 enables complex robotic systems to operate cohesively.

## DDS-Based Communication

ROS 2's major architectural shift from ROS 1 is its transition to Data Distribution Service (DDS) as the underlying communication middleware. DDS is a vendor-neutral, open standard for real-time, distributed systems that supports publish-subscribe communication patterns.

### Why DDS?

- **Real-time performance**: Guarantees timely delivery of critical data
- **Scalability**: Supports large numbers of participating nodes
- **Reliability**: Provides multiple Quality of Service (QoS) policies
- **Interoperability**: Allows nodes written in different languages to communicate
- **Security**: Built-in security features for commercial applications

### Quality of Service (QoS) Policies

ROS 2's QoS policies allow fine-tuning of communication characteristics based on the needs of specific data streams:

- **Reliability**: Choose between reliable (acknowledged) or best-effort delivery
- **Durability**: Configure history retention (volatile vs transient-local)
- **Deadline**: Specify timing requirements for data delivery
- **Liveliness**: Monitor the availability of publishers and subscribers

Example of setting QoS policy in Python:
```python
from rclpy.qos import QoSProfile, ReliabilityPolicy

# Create a QoS profile for sensor data (best effort, small history)
sensor_qos = QoSProfile(
    depth=10,
    reliability=ReliabilityPolicy.BEST_EFFORT
)

# Create a QoS profile for critical commands (reliable, larger history)
cmd_qos = QoSProfile(
    depth=20,
    reliability=ReliabilityPolicy.RELIABLE
)
```

## Execution Models

ROS 2 offers flexible execution models to handle various application requirements:

### Single-threaded Executor
Executes all callbacks sequentially in a single thread. Simple but may become a bottleneck for CPU-intensive operations.

### Multi-threaded Executor
Distributes callback execution across multiple threads, improving responsiveness for parallelizable tasks.

### Custom Executors
Advanced users can create specialized executors tailored to specific application requirements.

## Lifecycle Nodes

ROS 2 introduces lifecycle nodes for managing complex systems that require state management and initialization sequences. Lifecycle nodes go through well-defined states:

1. Unconfigured → Inactive (configure)
2. Inactive → Active (activate)
3. Active → Inactive (deactivate)
4. Inactive → Finalized (cleanup)

This is particularly important for mission-critical robotic applications where proper resource management and graceful transitions between states are essential.

## Parameter System

The parameter system in ROS 2 is distributed and dynamic, allowing nodes to:

- Declare parameters with types and constraints
- Set parameters at runtime
- Share parameters between nodes
- Save/load parameter configurations

Example parameter declaration:
```python
class MyNode(Node):
    def __init__(self):
        super().__init__('my_node')
        
        # Declare parameters with defaults and descriptions
        self.declare_parameter('max_velocity', 1.0, 
                              descriptor=ParameterDescriptor(description='Maximum allowed velocity'))
        self.declare_parameter('safety_radius', 0.5)
```

## Actions

Actions in ROS 2 provide a way to send goals to long-running processes and receive feedback. They're ideal for tasks like:

- Navigation to a specific location
- Manipulation sequences
- Calibration processes

Action clients can send goals, receive feedback during execution, and get results when complete. Actions also support preemption, allowing goals to be canceled or replaced.

## Package Management

ROS 2 uses the colcon build system for package management, which offers:

- Parallel builds for faster compilation
- Support for multiple programming languages
- Flexible workspace layouts
- Better dependency resolution

## Security in ROS 2

Commercial robotic deployments require robust security measures:

- **Authentication**: Verifying identity of nodes and users
- **Access Control**: Defining which entities can access specific resources
- **Encryption**: Protecting data during transmission
- **Audit**: Logging security-relevant events

## Practical Implementation Example

Let's put these concepts together with a comprehensive example of a ROS 2 node that implements a simple navigation system:

```python
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy
from geometry_msgs.msg import PoseStamped, Twist
from nav_msgs.msg import Odometry
from std_msgs.msg import Bool

class NavigationNode(Node):
    def __init__(self):
        super().__init__('navigation_node')
        
        # QoS profiles for different types of data
        qos_sensor = QoSProfile(depth=5, reliability=ReliabilityPolicy.BEST_EFFORT)
        qos_cmd = QoSProfile(depth=10, reliability=ReliabilityPolicy.RELIABLE)
        
        # Publishers and subscribers
        self.odom_sub = self.create_subscription(
            Odometry, '/odom', self.odom_callback, qos_sensor)
        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', qos_cmd)
        self.goal_sub = self.create_subscription(
            PoseStamped, '/move_base_simple/goal', self.goal_callback, 10)
        
        # Internal state
        self.current_pose = None
        self.target_pose = None
        self.is_navigating = False
        
        # Timer for navigation loop
        self.nav_timer = self.create_timer(0.1, self.navigation_loop)
        
        self.get_logger().info('Navigation node initialized')

    def odom_callback(self, msg):
        """Update current pose from odometry"""
        self.current_pose = msg.pose.pose

    def goal_callback(self, msg):
        """Receive new navigation goal"""
        self.target_pose = msg.pose
        self.is_navigating = True
        self.get_logger().info(f'New goal received: {msg.pose.position.x:.2f}, {msg.pose.position.y:.2f}')

    def navigation_loop(self):
        """Main navigation algorithm"""
        if not self.is_navigating or self.target_pose is None:
            return
            
        if self.current_pose is None:
            return  # Wait for odometry data
            
        # Calculate distance to goal
        dx = self.target_pose.position.x - self.current_pose.position.x
        dy = self.target_pose.position.y - self.current_pose.position.y
        distance = (dx**2 + dy**2)**0.5
        
        # Simple proportional controller
        cmd = Twist()
        if distance > 0.1:  # Not at goal yet
            cmd.linear.x = min(0.5, distance * 0.5)  # Move toward goal
            cmd.angular.z = 0.0  # Simplified rotation control
        else:
            cmd.linear.x = 0.0  # At goal
            cmd.angular.z = 0.0
            self.is_navigating = False
            self.get_logger().info('Reached goal!')
            
        self.cmd_pub.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = NavigationNode()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Interrupted by user')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
```

## Summary

ROS 2's architecture provides a robust foundation for building complex robotic systems. Its DDS-based communication, comprehensive QoS policies, lifecycle management, and security features make it suitable for both research and commercial applications. Understanding these architectural concepts is crucial for developing efficient, maintainable robotic applications.

The modular design of ROS 2 encourages separation of concerns, allowing developers to focus on specific aspects of robotic functionality while relying on the framework for communication and coordination between components.