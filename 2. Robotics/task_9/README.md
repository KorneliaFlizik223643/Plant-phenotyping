# Opentron OT-2

## Project Overview:

The OT-2 Digital Twin is a virtual representation of the Opentrons OT-2, a popular robotic liquid handling system used in labs.

## Directory structure

* `/meshes` directory contains STL files representing the meshes used in the simulation.
* `sim_class.py` is a python script containing classes and functions used in the simulation. It is well-commented for ease of understanding and modification. 
* `custom.urdf` is the custom urdf added to OT-2
* `ot_2_simulation_v6.urdf` is a standard ot-2 urdf

## Dependencies
Ensure you have the following dependencies installed before running the simulation:

- Python (3.6 or later)
- Microsoft Visual C++ (14.0 or greater)
- PyBullet

Installing PyBullet 
```
pip install pybullet
```

## Environment Setup
### Setting up the OT-2 Digital Twin ### 

Checkout the git tree:
```
git clone https://github.com/BredaUniversityADSAI/Y2B-2023-OT2_Twin.git
```

### Usage of Simulation
To utilize the functionalities provided by `sim_class.py` in your simulation, import the module as follows:

```
from sim_class import Simulation
#Example instantiation
sim = Simulation(num_agents=1)
```

## Simulation
### Working envelope 
Pipette corners coordinates
* Point 1 (-0.187, -0.1709, 0.1195)
* Point 2 (0.253, -0.1709, 0.1195)
* Point 3 (0.253, 0.2195, 0.1195)
* Point 4 (-0.187, 0.2195, 0.1195)
* Point 5 (-0.187, -0.1709, 0.2895)
* Point 6 (0.253, -0.1709, 0.2895)
* Point 7 (0.253, 0.2195, 0.2895)
* Point 8 (-0.187, 0.2195, 0.2895)

