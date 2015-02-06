Name:           ros-indigo-laser-joint-projector
Version:        1.0.9
Release:        0%{?dist}
Summary:        ROS laser_joint_projector package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/laser_joint_projector
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-calibration-msgs
Requires:       ros-indigo-cmake-modules
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-kdl-parser
Requires:       ros-indigo-orocos-kdl
Requires:       ros-indigo-roscpp-serialization
BuildRequires:  ros-indigo-calibration-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-kdl-parser
BuildRequires:  ros-indigo-orocos-kdl
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-roscpp-serialization

%description
Projects laser readings into a point cloud, based on a set of recorded joint
angles This package is experimental and unstable. Expect its APIs to change.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Feb 06 2015 Devon Ash <dash@clearpathrobotics.com> - 1.0.9-0
- Autogenerated by Bloom

