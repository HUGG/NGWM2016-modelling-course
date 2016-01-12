## Data visualization with **ParaView**  - outline

#### Post-processing
- Results can be post-processed to convert to `.vtk` files by double-clicking on the `ExportDB.bat` file
  - This runs a Python code that converts the output from the default format in Gale to a `.vtk` file that can be loaded in **ParaView**
  - Note: This uses the software **VisIt** for the conversion

#### Visualizing data in **ParaView**
- Loading data files in **ParaView**
  - File -> Open...
  - Gale output files:
    1. `FEM_Grid_pressure-mesh.#####`: Pressures on the FE grid
    2. `FEM_Grid_v-mesh.#####`: Strain rates and velocities on the FE grid
    3. `materialSwarm.#####`: Various field data values on the cloud of particles, including viscosity
  - Loading one time step versus a whole series of steps
- **ParaView** filter concept
  - Data in **ParaView** is treated like a stream. Data is loaded and can then "flow" into various filters to manipulate the data.

- Basic plotting
  - Field data on grid
    - Example of strain rates
      - Changing the contour color range
      - Changing the color scheme
  - Cloud particle data
    - Example of viscosity data
      - Changing the color scheme (again)
      - Using logrithmic color scaling
  - Velocity vectors
    - Scaling the velocity vectors
    - Decimating velocity fields
  - Contouring
  - Clipping

- More advanced Plotting
  - Splitting windows
  - Linking cameras
  - Adding text/time step
  - Using the calculator
  - Adding axes to the plot/manipulating the axis labels
  - Changing the velocity vector glyphs
  - Translating/rotating velocity vectors or the plotted data
  - Opacity, line widths/point sizes

- Saving output
  - Screenshots
    - Changing the effective resolution
  - Animations
  - **ParaView** states
