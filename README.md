# ROBOT SIMULATION PROJECT
This project aims to launch and simulate a robot in Gazebo. This repository serves as a guide for developing and simulating a robot. It highlights all the steps that should be followed to achieve the desired result.

## REQUIRED SOFTWARE
1. A CAD tool of your choice
2. Blender (With Phobos add-on)
3. ROS2 Jazzy
4. Gazebo Harmonic
5. Ubuntu or WSL2 

**TIP**
If your hardware cannot support the software mentioned above, you can use Github codespaces. By properly configuring it with ROS2 and VNC support, you can run the entire simulation in Codespaces.


## STEP 1: CAD MODELLING
Design your robot using any CAD tool of your preference. Assemble the robot and ensure that it is done correctly. Properly define the links and joints and ensure that the parts are properly separated in the assembly.

## STEP 2: URDF GENERATION
The next step is to generate the URDF. This will depend on the CAD tool used because some like On Shape and Fusion 360 can generate URDFs by downloading an add-on. If your CAD tool cannot generate the URDF, use Blender. Export the file to Blender in your desired format and use the Phobos add-on to generate the URDF. Ensure that all the links, joints and geometry are properly defined. Download the URDF and meshes. 

## STEP 3: SPAWNING THE ROBOT
The next step is to spawn your robot in Gazebo. The process is as follows;
1. Create a ROS2 workspace
2. Clone your project into the workspace
3. Build the worspace
4. Source the workspace
5. Launch the simulation
6. Verify the robot is spawned

![Robot Screenshot](Images/Robot.JPG)

If the robot doesn't spawn or Gazebo doesn't launch, troubleshooting will be required.
- Check if Gazebo Harmonic is installed correctly. 
- Check the URDF file paths.
- Ensure robot_state_publisher is running.

## SENSOR INTEGRATION
This step involves integrating sensors to the robot. Attach the sensor plug ins to the URDF. You can add your preffered sensors. In this project, a camera, Lidar Sensor and IMU have been attached. Ensure the URDF format is correct by checking the gazebo github page which has the format for a variety of sensors. Spawn the robot in Gazebo again to ensure that the sensora have been properly added. 

## CHALLENGES FACED
1. Generating meshes in Blender.
2. Fixing Gazebo launch errors.

## FUTURE IMPROVEMENTS
1. Making the robot autonomous.
2. Integrating more sensors. 

## AUTHOR
Vanessa Warera

