import curses
import time
from ur_controller import URController

def live_monitor(stdscr, robot_ip="192.168.0.100"):
    controller = URController(robot_ip)
    stdscr.nodelay(True)
    curses.curs_set(0)

    try:
        while True:
            stdscr.clear()

            try:
                data = controller.get_robot_data()
            except Exception as e:
                stdscr.addstr(0, 0, f"[!] Error reading robot data: {e}")
                stdscr.refresh()
                time.sleep(1)
                continue

            stdscr.addstr(0, 0, "🦾  UR Robot Live Monitor (press 'q' to quit)")
            stdscr.addstr(2, 0, f"Joint Positions : {['%.3f' % j for j in data['joint_positions']]}")
            stdscr.addstr(3, 0, f"TCP Pose        : {['%.3f' % p for p in data['tcp_pose']]}")
            stdscr.addstr(4, 0, f"TCP Force       : {['%.2f' % f for f in data['tcp_force']]}")
            stdscr.addstr(5, 0, f"Digital Inputs  : {data['digital_inputs']}")
            stdscr.addstr(6, 0, f"Digital Outputs : {data['digital_outputs']}")
            stdscr.addstr(7, 0, f"Program Running : {data['is_program_running']}")

            stdscr.refresh()
            time.sleep(0.25)

            if stdscr.getch() == ord('q'):
                break
    finally:
        controller.close()
        curses.endwin()

if __name__ == "__main__":
    curses.wrapper(live_monitor)
