from ur_controller import URController

def pick_and_place(controller: URController, cycles: int = 1):
    """
    Executes a pick-and-place loop.
    :param controller: URController instance
    :param cycles: Number of repetitions; -1 for infinite
    """
    pick_pose = (0.3, -0.2, 0.1, 0.0, 3.14, 0.0)
    lift_pose = (0.3, -0.2, 0.2, 0.0, 3.14, 0.0)
    place_pose = (0.4, 0.2, 0.1, 0.0, 3.14, 0.0)
    retreat_pose = (0.4, 0.2, 0.2, 0.0, 3.14, 0.0)

    iteration = 0
    while controller.running and (cycles == -1 or iteration < cycles):
        print(f"--- Pick and Place Cycle {iteration + 1} ---")
        controller.set_vacuum(True)
        controller.move_linear(pick_pose)
        controller.wait(0.2)

        controller.move_linear(lift_pose)
        controller.wait(0.1)

        controller.move_linear(place_pose)
        controller.wait(0.2)

        controller.set_vacuum(False)
        controller.wait(0.2)

        controller.move_linear(retreat_pose)
        controller.wait(0.1)

        iteration += 1

    print("✅ Pick-and-place complete.")
