import urx
import time
import signal

class URController:
    def __init__(self, robot_ip):
        self.robot = urx.Robot(robot_ip)
        self.running = True
        signal.signal(signal.SIGINT, self._handle_interrupt)

    def _handle_interrupt(self, signum, frame):
        print("\n[!] Interrupt received — stopping.")
        self.running = False

    def close(self):
        self.robot.close()

    def wait(self, seconds):
        time.sleep(seconds)

    def move_joint(self, joints, acc=1.0, vel=0.5):
        self.robot.movej(joints, acc=acc, vel=vel)

    def move_linear(self, pose, acc=0.5, vel=0.25):
        self.robot.movel(pose, acc=acc, vel=vel)

    def set_vacuum(self, state: bool, output=0):
        self.robot.set_digital_out(output, state)

    def get_robot_data(self):
        return {
            "joint_positions": self.robot.getj(),
            "tcp_pose": self.robot.getl(),
            "tcp_force": self.robot.get_tcp_force(),
            "analog_inputs": self.robot.get_analog_in(),
            "digital_inputs": self.robot.get_digital_in(),
            "digital_outputs": self.robot.get_digital_out(),
            "is_program_running": self.robot.secmon.is_program_running()
        }
