from ur_controller import URController
from programs.pick_place import pick_and_place

def main():
    controller = URController("192.168.0.100")
    try:
        pick_and_place(controller, cycles=5)  # Or use -1 for infinite
    finally:
        controller.close()

if __name__ == "__main__":
    main()
