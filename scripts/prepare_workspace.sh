#!/bin/bash

#========= Global Variables ========
work_space_folder=$(pwd)

#========     Main code     =========

sudo apt update
sudo apt upgrade -y # Corrected the command


echo "Criando venv"
cd ../
python3 -m venv venv
source venv/bin/activate


echo "Clonando rep"
cd ./src
git clone https://github.com/ros/ros_tutorials.git -b humble 


echo "Instalando rodesp"
sudo apt install python3-rosdep -y
sudo rosdep init
rosdep update


cd ..
rosdep install -i --from-path src --rosdistro humble -y


echo "Instalando colcon common extensions"
sudo apt install python3-colcon-common-extensions

echo "Building Workspace"
(colcon build & wait $!; pkill -INT colcon) # Builds and sends SIGINT signal to terminate colcon if it gets stuck
echo ""


echo "Backing to Workspace root folder"
cd $work_space_folder # Goes back to the workspace folder
echo ""


echo "Executing the local_setup.sh"
cd "$work_space_folder"
source "../install/local_setup.bash" # Execute this necessary file
echo ""


# Starting the turtle moving program
ros2 run entregador_de_jornal jornaleiro

echo "Done ;) xD" # End of the code
