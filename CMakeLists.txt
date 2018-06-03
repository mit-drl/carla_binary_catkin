cmake_minimum_required(VERSION 2.8.3)
project(carla_binary_catkin)

include(ExternalProject)
set(CMAKE_BUILD_TYPE Release)

find_package(catkin REQUIRED)

set(CARLA_URL https://drive.google.com/uc?id=1ZtVt1AqdyGxgyTm69nzuwrOYoPUn_Dsm)
set(CARLA_VERSION 0.8.2)

catkin_package()

ExternalProject_Add(carla_binary_catkin
  #NOTE: The following is used to avoid unnecessary downlads when debugging.
  #URL ${CMAKE_SOURCE_DIR}/CARLA_${CARLA_VERSION}.tar.gz
  DOWNLOAD_COMMAND
    python ${CMAKE_SOURCE_DIR}/scripts/download_from_gdrive.py  ${CARLA_URL} \\
      CARLA_${CARLA_VERSION}.tar.gz
  PATCH_COMMAND tar -xzf ../CARLA_${CARLA_VERSION}.tar.gz
  UPDATE_COMMAND ""
  CONFIGURE_COMMAND ""
  BUILD_COMMAND ""
INSTALL_COMMAND
  # Copy Carla binaries and libraries.
  cp -r <SOURCE_DIR>/CarlaUE4/ ${CATKIN_DEVEL_PREFIX}/${CATKIN_PACKAGE_SHARE_DESTINATION}/ &&
  cp -r <SOURCE_DIR>/Engine/ ${CATKIN_DEVEL_PREFIX}/${CATKIN_PACKAGE_SHARE_DESTINATION}/ &&
  mkdir -p ${CATKIN_DEVEL_PREFIX}/${PYTHON_INSTALL_DIR}/ &&
  cp -r <SOURCE_DIR>/PythonClient/carla/ ${CATKIN_DEVEL_PREFIX}/${PYTHON_INSTALL_DIR}/)


catkin_add_nosetests(test/test_carla_catkinization.py)
